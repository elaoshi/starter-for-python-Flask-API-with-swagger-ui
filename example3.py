from flask import Flask, request
from flask_restplus import Resource, Api

from flask_restplus import reqparse


app = Flask(__name__)
api = Api(app)


@api.route('/my-resource/<id>', endpoint='my-resource')
@api.doc(params={'id': 'An ID'})
class MyResource(Resource):

    def get(self, id):
        return {}

    
    @api.doc(responses={403: 'Not Authorized'},params={'ano':'ano'})
    def post(self, id):
        # if anoId is not None:
        
        ano = request.args.get("ano")
        parser = reqparse.RequestParser()
        # parser.add_argument('ano', type=int, help='Rate cannot be converted')
        parser.add_argument('ano')
        args = parser.parse_args()

        return {'id':id,'ano':ano}

        api.abort(403)