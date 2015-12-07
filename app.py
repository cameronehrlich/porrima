from flask import Flask, jsonify
from datetime import date, timedelta

import parser
import stockquote

app = Flask(__name__)


@app.route('/reports/today')
def reports_today():
    output_list = parser.earnings_report_for_date()
    return jsonify(earning_events=output_list)


@app.route('/reports/future/<int:days>')
def reports_future(days):
    date_object = date.today() + timedelta(days=days)
    output_list = parser.earnings_report_for_date(date_object=date_object)
    return jsonify(earning_events=output_list)


@app.route('/quote/<symbol>')
def quote(symbol):
    return jsonify(stockquote.from_yahoo(symbol))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
