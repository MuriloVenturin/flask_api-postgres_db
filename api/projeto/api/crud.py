from flask import request
from flask_restplus import Resource, fields
from sqlalchemy.exc import OperationalError

from projeto.restplus import api
from projeto.entity.crud.model import Teste
from projeto.constants import CodeHttp

ns = api.namespace('crud', description='This operation will record a data in the database')

teste_model = ns.model('teste_model', {'USUARIO': fields.String(required=True,
                                            description='USUARIO',
                                            example="usuario"),
                                       'STATUS': fields.String(
                                            required=True,
                                            description='STATUS',
                                            example="bom")
                                            })

@ns.route('')
class TutorApi(Resource):

    @ns.expect(teste_model)
    def post(self):

        """
        {
            "USUARIO": "usuario",
            "STATUS": "bom"
        }
        :return:
        """
        input_request = request.get_json()
        try:  # caso o banco caia

            new_tutor = Teste(input_request['USUARIO'],
                              input_request['STATUS'])
            new_tutor.insert()
        except OperationalError:
            return {'error': 'Error durante a conexão com o banco'}, CodeHttp.ERROR_500
        return new_tutor.json()


