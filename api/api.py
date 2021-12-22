import time
import flask
import os
import json
import neomodel
import models

# DB_URL = os.getenv("DB_URL", "bolt://neo4j:foobar@localhost:7687")
DB_URL = os.getenv(
    "DB_URL",
    "neo4j+s://neo4j:MZaKywDYwm1CdjnI_b5oFwF9Zi8CEwZPhT9nbRdEcOs@ea862a8f.databases.neo4j.io",
)


def create_an_item():
    neomodel.db.set_connection(DB_URL)
    models.Item(name="Something Something Dark Side").save()


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
    # Comment the above line and uncomment the following two to launch the app
    flask_app = create_app()
    # At this point, the neomodel.db object is configured and valid
    flask_app.run(host="localhost", port=8000, debug=True)
