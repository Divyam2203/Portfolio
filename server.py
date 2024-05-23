from flask import Flask, render_template, request
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', 'a',newline = "") as csvfile:
        data_row = []
        data_row.append(data['email'])
        data_row.append(data['subject'])
        data_row.append(data['message'])
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(data_row)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      try:
        data = request.form.to_dict()
        write_to_csv(data)
        return html_page('/thankyou.html')
      except: 
        return "ERROR. did not save to database!"
    else:
        return "something went wrong"
