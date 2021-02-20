from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []
class App(Resource):
    
    def post(self):
        data = request.json
        items.append(data)
        return data
        
        
    def get(self):
        return items
    
api.add_resource(App, '/')

if __name__ == '__main__':
    app.run(port=5000, debug=True)