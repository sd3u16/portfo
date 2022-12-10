from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('universe/universe/index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f'universe/universe/{page_name}')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='\n', mode='a') as database2:
        email = data["email"]
        subject = data['subject']
        message = data['message']
        csvWriter = csv.writer(database2, delimiter=',', quotechar='"', quoting =csv.QUOTE_MINIMAL)
        csvWriter.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect(f'thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'


if __name__ == '__main__':
    app.run()
