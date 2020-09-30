import logging
import traceback

from flask_restplus import Api
import settings
from projeto.constants import CodeHttp, Message

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Documentação - API',
          description='Endpoints')


@api.errorhandler
def default_error_handler(e):
    log.exception(Message.ERROR_NOT_TREATMENT)

    if not settings.FLASK_DEBUG:
        return {'message': Message.ERROR_NOT_TREATMENT}, CodeHttp.ERROR_500
