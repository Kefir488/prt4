import csv
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

messages = []

def write_to_file(data):
    with open('database.txt','a') as database:
           name = data['name']
           email = data['email']
           message = data['message']
           database.write(f'\nname:{name}, email:{email}, message:{message}')

def write_to_csv(data):
    with open('database.csv','a') as database2:
           email = data['email']
           subject = data['subject']
           message = data['message']
           csv_writer = csv.writer(database2,delimiter=';',quoting=csv.QUOTE_MINIMAL,lineterminator = '\n')
           csv_writer.writerow([subject,email,message])
           

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods = ['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'       
    else:
       return 'something went wrong, please try again'