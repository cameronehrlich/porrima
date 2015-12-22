from flask import Flask, jsonify
from magicdate import magicdate

import parser
import stockquote

app = Flask(__name__)


@app.route('/')
def hello():
    return 'reporting_on_date/ \n date_for_symbol/ \n current_quote/'


@app.route('/reporting_on_date/<date_string>')
def reports_for_date(date_string):
    try:
        date_object = magicdate(date_string)
        output_list = parser.earnings_reports_on_date(date_object)
        return jsonify(earnings_reports=output_list)
    except:
        print('Could not parse date')
        return jsonify(earning_events=None)


@app.route('/date_for_symbol/<symbol>')
def date_for_symbol(symbol):
    date_object = parser.earnings_report_date_for_symbol(symbol)
    return jsonify(date=date_object)


@app.route('/current_quote/<symbol>')
def quote_for_symbol(symbol):
    return jsonify(stockquote.from_yahoo(symbol))
