
from flask import Flask,jsonify,request,render_template
import csv
from libs.cases import get_covid_cases
from libs.datetime import getDate
# from libs import reader
# from libs import countries
# creating out flask object
app = Flask(__name__)

# creating our app decorator
@app.route("/", methods=["GET"])
@app.route("/api", methods=["GET"])
@app.route("/api/<date>", methods=["GET"])

# returning an API end point
def index(date=None):
    if date is None:
        yesterday = getDate()
        cases = get_covid_cases(yesterday)
    else:
        cases = get_covid_cases(date)
    return  render_template('index.html', cases=cases)


if __name__ == "__main__":
    app.run(debug=True)


    
