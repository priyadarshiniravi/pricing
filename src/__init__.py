from flask import Flask

application = Flask(__name__)
application.config['DEBUG'] = True

import src.services.pricing_engine_service