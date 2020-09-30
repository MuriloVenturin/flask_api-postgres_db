# Flask settings
# FLASK_SERVER_NAME='localhost:9000'
# FLASK_HOST = 'localhost'
FLASK_SERVER_NAME = '0.0.0.0:9009'
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 9009
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

SQL_CONNECTION_STRING = 'postgresql://postgres:changeme@localhost:5432/postgres'

