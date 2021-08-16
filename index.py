from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api
import time
import random

app = Flask(__name__)
cors = CORS(app)
api = Api(app)

class timeInit():
	start_time = 0

class action(Resource):
	def get(self):
		return {'status': 'active',
				'ms': int((time.time() - timeInit.start_time)*1000),
				'score': random.randint(0, 500)}

	def post(self):
		timeInit.start_time = time.time() - 2
		return {'status': 200}

@app.errorhandler(Exception)
def handleException(e):
	return {'status': 'error',
			'message': "There was an error running API."}, 500

@app.after_request
def after_request(response):
	header = response.headers
	header['Access-Control-Allow-Origin'] = '*'
	return response

api.add_resource(action, '/arduino')

if __name__ == '__main__':
	app.run(port=5000, debug=True)