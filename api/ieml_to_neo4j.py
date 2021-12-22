import os
import sys
import json
import neomodel
import models

## LOCALHOST DB (via docker for example)
DB_URL = os.getenv("DB_URL", "bolt://neo4j:foobar@localhost:7687")

## Permanent cloud Neo4j DB : https://console.neo4j.io/#databases/ea862a8f/detail
# DB_URL = os.getenv(
#     "DB_URL",
#     "neo4j+s://neo4j:MZaKywDYwm1CdjnI_b5oFwF9Zi8CEwZPhT9nbRdEcOs@ea862a8f.databases.neo4j.io",
# )


def parse_json_and_feed_neo4j(ieml_json_file, ontology_id, ontology_name):
    input_file = open("iemlgraph.json")
    json_array = json.load(input_file)
    neomodel.db.set_connection(DB_URL)
    nodes_list = []
    relations_list = []
    neo4j_nodes_dict = {}

    for node in json_array["nodes"]:
        node_details = {"class": None, "id": None, "names": None}
        node_details["class"] = node["class"]
        node_details["id"] = node["id"]
        node_details["names"] = node["names"]
        nodes_list.append(node_details)

    for relation in json_array["relations"]:
        relation_details = {"class": None, "attributes": None, "from": None, "to": None}
        relation_details["class"] = relation["class"]
        relation_details["attributes"] = relation["attributes"][1]
        relation_details["from"] = relation["subject"]
        relation_details["to"] = relation["object"]
        relations_list.append(relation_details)

    neo4j_ontology = get_or_create_ontology_neo4j_node(ontology_id, ontology_name)

    for node in nodes_list:
        ## Get if exist, the node from Neo4j DB in current Ontology
        neo4j_node = get_node_in_ontology(neo4j_ontology.uid, node["id"])

        if neo4j_node:
            neo4j_node = neo4j_node[0]
        else:
            create_neo4j_node(node, neo4j_ontology)

        neo4j_nodes_dict[node["id"]] = neo4j_node
        # print(neo4j_ontology.ontologies_nodes.all())

    for relation in relations_list:
        create_relationships_between_nodes(relation, neo4j_nodes_dict)


def get_or_create_ontology_neo4j_node(ontology_id, ontology_name):
    neo4j_ontology = models.IemlOntology.nodes.get_or_none(ieml_id=ontology_id)
    if neo4j_ontology == None:
        print("CREATING IemlOntology Neo4j node")
        neo4j_ontology = models.IemlOntology(
            ieml_id=ontology_id, ieml_name=ontology_name
        ).save()
        print("neo4j_ontology " + neo4j_ontology.uid)
    return neo4j_ontology


def get_node_in_ontology(ontology_id, node_id):
    neo4j_node_query = """MATCH (o:IemlOntology) WHERE o.uid="{ontology_ieml_uid}" MATCH (o:IemlOntology)-[:HAS_NODE|:HAS_COMPONENT]->(n) WHERE n.ieml_id={node_ieml_id} AND ((n:IemlNode) OR (n:IemlComponent)) RETURN n""".format(
        ontology_ieml_uid=str(ontology_id), node_ieml_id=node_id
    )
    results, meta = neomodel.db.cypher_query(neo4j_node_query)
    neo4j_node = [models.IemlNode.inflate(row[0]) for row in results]
    # print("neo4j_node_names === : " + str(neo4j_node[0].ieml_names))
    # print("neo4j_node[0] " + str(neo4j_node))
    return neo4j_node


def create_neo4j_node(node, neo4j_ontology):
    if node["class"] == "NODE":
        print("CREATING IemlNode Neo4j node: " + str(node["id"]))
        neo4j_node = models.IemlNode(
            ieml_id=node["id"], ieml_names=node["names"]
        ).save()
        rel = neo4j_ontology.ontologies_nodes.connect(neo4j_node)

    if node["class"] == "COMPONENT":
        print("CREATING IemlComponent Neo4j node " + str(node["id"]))
        neo4j_node = models.IemlComponent(
            ieml_id=node["id"], ieml_names=node["names"]
        ).save()
        rel = neo4j_ontology.ontologies_components.connect(neo4j_node)

    return neo4j_node


def create_relationships_between_nodes(relation, neo4j_nodes_dict):
    if relation["from"] is not None:
        from_node = neo4j_nodes_dict.get(relation["from"])
        # from_node_type = type(from_node).__name__
        if (relation["to"] is not None) and (from_node is not None):
            to_node = neo4j_nodes_dict.get(relation["to"])

            if to_node is not None:
                to_node_type = type(to_node).__name__

                if to_node_type == "IemlNode":
                    rel = from_node.composition_tonodes.connect(
                        to_node, {"attributes": relation["attributes"]}
                    )
                if to_node_type == "IemlComponent":
                    rel = from_node.composition_tocomponents.connect(
                        to_node, {"attributes": relation["attributes"]}
                    )


if __name__ == "__main__":
    ontology_id = "1"
    ontology_name = "IEML Grammar"
    parse_json_and_feed_neo4j("iemlgraph.json", ontology_id, ontology_name)
