"""Currency converter web API

This application converts currency based on exchange rates
published by European Central Bank.

Module `flask` is required to be installed
within the Python environment you are running this in.

Created by Samuel Mensak.

"""

import currency_converter
import flask
from flask import request, jsonify, current_app

# flask setup
app = flask.Flask(__name__)
app.config["DEBUG"] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

# API GET method
@app.route('/currency_converter', methods=['GET'])

def api_currency_converter():
    
    # check params
    if 'input_currency' in request.args:
        input_currency = str(request.args['input_currency'])
    else:
        return "Error: No input currency provided."

    if 'amount' in request.args:
        amount = str(request.args['amount'])
    else:
        return "Error: No amount provided."

    # if output currency given convert to it
    if 'output_currency' in request.args:
        output_currency = str(request.args['output_currency'])
        result = currency_converter.main(['-i', input_currency,
                                          '-a', amount,
                                          '-o', output_currency])
    # else convert to all currencies availible
    else:
        result = currency_converter.main(['-i', input_currency,
                                          '-a', amount])
    # return result (JSON)
    return result

app.run()
