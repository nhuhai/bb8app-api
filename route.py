
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask_restful import Resource, Api
import config

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
  if config.app['debug']:
    app.run(debug = True, threaded = True, host = config.app['host'], port = config.app['port'])
  else:
    app.run(debug = False, threaded = True)
