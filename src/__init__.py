from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['DEBUG'] = True
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://saranganesan:whatever@tw-flask-demo.cv1vih0jkyyw.us-west-2.rds.amazonaws.com/Home_Service'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(application)

import src.services.pricing_engine_service