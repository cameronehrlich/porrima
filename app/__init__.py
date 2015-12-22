from flask import Flask, jsonify
from magicdate import magicdate

import parser
import stockquote

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/reporting_on_date/<date_string>')
def reports_for_date(date_string):
    try:
        date_object = magicdate(date_string)
    except Exception, e:
        return jsonify(earning_events=None)
    output_list = parser.earnings_reports_on_date(date_object)
    return jsonify(earning_events=output_list)


@app.route('/date_for_symbol/<symbol>')
def date_for_symbol(symbol):
    date_object = parser.earnings_report_date_for_symbol(symbol)
    return jsonify(date=date_object)


@app.route('/current_quote/<symbol>')
def quote_for_symbol(symbol):
    return jsonify(stockquote.from_yahoo(symbol))
