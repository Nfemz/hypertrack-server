from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)

if __name__ == '__main__':
    postgres_uri = 'postgresql://localhost/hyper-track'
else:
    postgres_uri = 'postgres://rtsxdpgdxdnmjb:e88e7ac4409a75ca38a3b3b702b45942416a56db54b1a87eaf2ace51f00c05b1@ec2-54-198-73-79.compute-1.amazonaws.com:5432/d31i7r7eemsjrq'
    
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = postgres_uri

db = SQLAlchemy(app)

ma = Marshmallow(app)

api = Api(app)