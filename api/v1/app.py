#!/usr/bin/python3
"""
Status of your API
"""
from api.v1.views import app_views
from flask import Flask
from flask_cors import CORS
from models import storage
import os

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    """ json 404 page """
    return {"error": "Not found"}, 404


@app.teardown_appcontext
def close_db(error):
    """Close the database at the end of the request"""
    storage.close()


if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)
