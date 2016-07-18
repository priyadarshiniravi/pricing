import flask
from flask import request

from src import application


@application.route('/')
def hello():
    return 'Hello World!!!!'


@application.route('/host-pricing-engine/compute-price', methods=['POST'])
def calculate_price():
    host_split = request.form['host_split']
    guest_price = request.form['guest_price']
    channel_fees = request.form['channel_fees']
    vat_percentage = request.form['vat_percentage']
    floor_price = request.form['floor_price']

    return flask.jsonify(host_share=50.0,
                         ofs_share=5000.0,
                         vat=90.0
                         )
