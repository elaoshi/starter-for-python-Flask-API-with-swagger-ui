from flask import Flask
from flask_restplus import Api, Resource , fields

flask_app = Flask(__name__)
app = Api(app = flask_app , 
        version='1.0.0', 
        title='Eric Test APT',
        description='A simple Test API',)

name_space = app.namespace('starter', description='Main Eric Starter APIs')

tmodel = app.model('Test', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'detail': fields.String(required=True, description='The task details')
})


@name_space.route("/",doc={'params':{'global_id': 'An ID'}})
@name_space.doc(responses={403: 'Not Authorized' , 200:'Success'})
class MainClass(Resource):
	def get(self):
        # test get function
		return {
			"status": "return data"
		}

	def post(self):
        # test post function
		return {
			"status": "return Posted data"
		}