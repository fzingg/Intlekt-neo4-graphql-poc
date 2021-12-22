# IEML Ontology to Neo4J nodes script and React Graphin test

## Installation

```
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    yarn install
```

## Running Flask and displaying Graphin Graph example

`npm start`

Open [http://localhost:8000](http://localhost:8000) to view it in the browser.


## Running the IEML_TO_NEO4J script

This script Parses a given IEML Ontology JSON file and feeds the Neo4j DB Nodes and RELATIONS accordingly:

`python3 api/ieml_to_neo4j.py`

Before running the script you must :
+ Run a Neo4j DB (see next chapter)
+ Set in the `api/ieml_to_neo4j.py`  
file these 3 params:
 * ontology_id
 * ontology_name
 * json graph file path
```
if __name__ == "__main__":
    ontology_id = "1"
    ontology_name = "IEML Grammar"
    parse_json_and_feed_neo4j("iemlgraph.json", ontology_id, ontology_name)
```

## Running the Neo4j DB

There are 2 ways to run a persistent Neo4j DB :

- Locally with a docker
- Remotely with a Neo4j AuraDB cloud already set up



### Locally with a docker

Clone this Neo4j 4.4.0 repo : [docker repo](https://github.com/fzingg/neo4j-docker.git)

run `docker-compose up`

Open [http://127.0.0.1:7474/browser/](http://127.0.0.1:7474/browser/) to view it in the browser.

In the browser, for the first time, you have to update the password of the DB : 

The first time enter that:
- User: neo4j
- Password: foobar

Then it will ask you to set up the new password:

- **foobar**

In `ieml_to_neo4j.py`:
```
DB_URL = os.getenv("DB_URL", "bolt://neo4j:foobar@localhost:7687")
```


### Remotely with a Neo4j AuraDB cloud already set up

Neo4j AuraDB cloud DB has been set up : [https://console.neo4j.io](https://console.neo4j.io)

Credentials to login to the account and access the DB browser:
- Email: fredzingg@gmail.com
- Password: Ieml-sandbox-27

Can access to the **IEML-neo4j** by clicking on the **Open with** -> Neo4j Browser

In `ieml_to_neo4j.py`:
```
## Permanent cloud Neo4j DB 
# DB_URL = os.getenv(
#     "DB_URL",
#     "neo4j+s://neo4j:MZaKywDYwm1CdjnI_b5oFwF9Zi8CEwZPhT9nbRdEcOs@ea862a8f.databases.neo4j.io",
# )
```