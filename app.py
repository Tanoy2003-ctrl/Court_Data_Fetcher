from flask import Flask, render_template, request
from scraper import fetch_case_details

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']

    details = fetch_case_details(case_type, case_number, filing_year)
    return details or "No details found."

if __name__ == '__main__':
    app.run(debug=True)
