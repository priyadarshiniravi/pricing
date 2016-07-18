import flask

from src import application


@application.route('/')
def hello():
    return 'Hello World!!!!'


@application.route('/host-pricing-engine/compute-price', methods=['POST'])
def calculate_price():
    return flask.jsonify(host_share=50.0,
                         ofs_share=5000.0,
                         vat=90.0
                         )
