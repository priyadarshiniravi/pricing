import flask
from flask import request

from src import application


@application.route('/')
def hello():
    return 'Hello World!!!!'


@application.route('/host-pricing-engine/compute-price', methods=['POST'])
def calculate_price():
    json = request.get_json()
    try:
        print(json['host_split'])
        print(json['guest_price'])
        print(json['channel_fees'])
        print(json['vat_percentage'])
        print(json['floor_price'])
    except KeyError:
        return "Invalid format", 400

    return flask.jsonify(host_share=50.0,
                         ofs_share=5000.0,
                         vat=90.0
                         )
