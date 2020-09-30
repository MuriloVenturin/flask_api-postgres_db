import logging.config
import os
from flask import Flask, Blueprint
import settings
from projeto.restplus import api as api
from flask_cors import CORS

from projeto.extensions import (
    bcrypt,
    login_manager,
    db
)

# TODO: Melhorar o nome dessas variaveis
from projeto.api.crud import ns as crud

from settings import *

app = Flask(__name__,  template_folder='./projeto/templates', )
CORS(app)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), './logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

def configure_app(flask_app):
    """
    Configures FLASK APP
    :param flask_app: the flask app of the application
    :return:
    """
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['SECRET_KEY'] = '<---YOUR_SECRET_FORM_KEY--->'
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = SQL_CONNECTION_STRING


def register_blueprints(flask_app, new_api, bp_posts):
    """Manages blueprints,
    a collection of routes and other app-related functions
    that can be registered on a real application later"""
    flask_app.register_blueprint(bp_posts)
    return None

def register_extensions(flask_app, new_api, bp_posts):
    """
    Registers Flask Extensions

    :param flask_app: A Flask APP
    :param new_api: A Flask API
    :return:
    """
    # Initialize API class with the given flask_blueprint

    new_api.init_app(bp_posts)
    bcrypt.init_app(flask_app)
    login_manager.init_app(flask_app)
    db.init_app(flask_app)
    return None

def register_namespaces_in_api(new_api):
    """
    Will register namespaces in API module
    :param new_api:
    :return:
    """
    new_api.add_namespace(crud)

    return None

def initialize_app(flask_app,new_api):
    """
    WIll initialize flask APP
    :param flask_app:
    :param new_api:
    :return:
    """
    bp_posts = Blueprint('api', __name__)

    configure_app(flask_app)
    register_extensions(flask_app, new_api, bp_posts)
    register_namespaces_in_api(new_api)
    register_blueprints(flask_app, new_api, bp_posts)    

def main():
    initialize_app(app, api)
    log.info('>>>>> Ao startar o server será com as uris http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    # app.run(host=settings.FLASK_HOST, port=settings.FLASK_PORT, debug=False)
    app.run(host=settings.FLASK_HOST, port=settings.FLASK_PORT, debug=settings.FLASK_DEBUG)
if __name__ == "__main__":
    main()