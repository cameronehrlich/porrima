from flask import Flask, jsonify
from datetime import date
from datetime import timedelta

app = Flask(__name__)

import parser
import stockquote


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/reports/today')
def reports_today():
    output_list = parser.earnings_reports_on_date()
    return jsonify(earning_events=output_list)


@app.route('/reports/future/<int:days>')
def reports_future(days):
    date_object = date.today() + timedelta(days=days)
    output_list = parser.earnings_reports_on_date(date_object=date_object)
    return jsonify(earning_events=output_list)


@app.route('/date/<symbol>')
def date_for_symbol(symbol):
    date_object = parser.earnings_report_date_for_symbol(symbol)
    return jsonify(date=date_object)


@app.route('/quote/<symbol>')
def quote_for_symbol(symbol):
    return jsonify(stockquote.from_yahoo(symbol))
