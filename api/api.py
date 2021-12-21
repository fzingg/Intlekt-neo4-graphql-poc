import time
import flask
import os
import json
import neomodel
import models

DB_URL = os.getenv("DB_URL", "bolt://neo4j:foobar@localhost:7687")


def create_an_item():
    neomodel.db.set_connection(DB_URL)
    models.Item(name="Something Something Dark Side").save()


def parse_json_and_feed_neo4j():
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

    neo4j_ontology = models.IemlOntology.nodes.get_or_none(ieml_id="1")
    if neo4j_ontology == None:
        print("CREATING IemlOntology Neo4j node")
        neo4j_ontology = models.IemlOntology(
            ieml_id="1", ieml_name="Ieml grammar"
        ).save()
        print("neo4j_ontology " + neo4j_ontology.uid)
        # neo4j_ontology = models.IemlOntology.nodes.get_or_none(ieml_id="1")

    for node in nodes_list:

        ## Get if exist, the node from Neo4j DB in current Ontology
        neo4j_node_query = """MATCH (o:IemlOntology) WHERE o.uid="{ontology_ieml_uid}" MATCH (o:IemlOntology)-[:HAS_NODE|:HAS_COMPONENT]->(n) WHERE n.ieml_id={node_ieml_id} AND ((n:IemlNode) OR (n:IemlComponent)) RETURN n""".format(
            ontology_ieml_uid=str(neo4j_ontology.uid), node_ieml_id=node["id"]
        )

        results, meta = neomodel.db.cypher_query(neo4j_node_query)
        neo4j_node = [models.IemlNode.inflate(row[0]) for row in results]
        # print("neo4j_node_names === : " + str(neo4j_node[0].ieml_names))
        # print("neo4j_node[0] " + str(neo4j_node))

        if neo4j_node:
            neo4j_node = neo4j_node[0]
        else:
            if node["class"] == "NODE":
                print("CREATING IemlNode Neo4j node")
                neo4j_node = models.IemlNode(
                    ieml_id=node["id"], ieml_names=node["names"]
                ).save()
                rel = neo4j_ontology.ontologies_nodes.connect(neo4j_node)

            if node["class"] == "COMPONENT":
                print("CREATING IemlComponent Neo4j node")
                neo4j_node = models.IemlComponent(
                    ieml_id=node["id"], ieml_names=node["names"]
                ).save()
                rel = neo4j_ontology.ontologies_components.connect(neo4j_node)

        print("neo4j_node --> " + str(neo4j_node))
        neo4j_nodes_dict[node["id"]] = neo4j_node
        # print(neo4j_ontology.ontologies_nodes.all())

    for relation in relations_list:
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


def create_app():
    """
    This is the original way presented to create a class. Please note
    the inline comments throughout
    """
    # In this example a Flask application is created explicity.
    app = flask.Flask(__name__)
    neomodel.config.DATABASE_URL = DB_URL

    @app.route("/time")
    def get_current_time():
        return {"time": time.time()}

    # At this point, the neomodel.db object has been initialised as expected
    @app.route("/items", methods=["GET"])
    def get_all_items():
        # !!! NOTICE ADDITION OF THIS INITIALISATION STEP !!!
        import models

        return {"items": [item.name for item in models.Item.nodes]}

    return app


if __name__ == "__main__":
    # !!!PRIOR TO RUNNING THE APP, CREATE AT LEAST ONE Item IN THE DATABASE!!!
    # create_an_item()
    parse_json_and_feed_neo4j()
    # Comment the above line and uncomment the following two to launch the app
    flask_app = create_app()
    # At this point, the neomodel.db object is configured and valid
    flask_app.run(host="localhost", port=8000, debug=True)
