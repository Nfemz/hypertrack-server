from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

data = []
class App(Resource):
    parser = reqparse.RequestParser()
    
    def post(self):
        key = data.length + 1
        data.push({key : App.parser.parse_args()})
        
    def get(self):
        return data
    
api.add_resource(App, '/')

if __name__ == '__main__':
    app.run(port=5000, debug=True)