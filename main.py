import json
from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

## Resource class
class Ambiente(Resource):
    def post(self):
        ambiente = request.json
        with open('ambientes.json','r+') as ambientes:
            content = json.loads(ambientes.read())
            content.append(ambiente)
            ambientes.seek(0)
            ambientes.write(json.dumps(content))

        return {'status': 'OK', 'mensaje':'Creado'}, 201

    def get(self):
        with open('ambientes.json','r') as ambientes:
            content = json.loads(ambientes.read())
            return content, 200

##
## Actually setup the Api resource routing here
##
api.add_resource(Ambiente,'/ambientes')

if __name__ == '__main__':
    app.run(debug=True)