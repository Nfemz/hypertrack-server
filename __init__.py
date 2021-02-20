from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class App(Resource):
    parser = reqparse.RequestParser()
    def post(self):
        data = App.parser.parse_args()
        print(data)
        return data, 200
    
api.add_resource(App, '/')

app.run(port=5000, debug=True)