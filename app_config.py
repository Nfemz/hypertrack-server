from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/hyper-track'

db = SQLAlchemy(app)

ma = Marshmallow(app)

api = Api(app)

db.create_all()