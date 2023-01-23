#!/usr/bin/env python
# encoding: utf-8
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_swagger_ui import get_swaggerui_blueprint

from routes import api

app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

app.register_blueprint(api.get_blueprint())

app.config['MONGODB_SETTINGS'] = {
    'db': 'lod_database',
    'host': 'localhost',
    'port': 27017
}
db_client = MongoEngine()
db_client.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
