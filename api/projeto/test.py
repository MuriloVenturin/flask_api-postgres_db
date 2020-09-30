#flask-restplus
@api.route('/api')
class repository(Resource):
    def get(self):
        try:
            person = People.query.filter_by(idpeople=request.get_json()['id']).first()        
            return json.dumps(People.toDict(person))            
        except:
            return "Usuário não existente."