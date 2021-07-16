import json
import os.path
import pymongo
from werkzeug.utils import secure_filename

from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify

from form import SignUpForm, LoginForm

app = Flask(__name__)
app.secret_key = "kjjjgjgkjlhuaiy7u"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('All fields are required.')
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('All fields are required.')
    else:
        connection_string = "mongodb+srv://ksp1510:kishan@cluster0.syoit.mongodb.net/db_rental?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority"
        myclient = pymongo.MongoClient(connection_string)
        db = myclient.users
        Users = db["users"]
        # Insert Record
        connection_customer = db["users"]
        mydict = {"fname": "John", "lname": "Bellion", "add": "65 Yorkland Blvd, Toronto", "pin": "L6P4M5",
                  "contact": "+14165640861", "email": "John43@gmail.com", "userid": "John45", "password": "JohnBellion"}
        mydict2 = {"fname": "Kishan", "lname": "Patel", "add": "235 Pharmacy Ave, Toronto", "pin": "M1L3G1",
                   "contact": "+14165242361", "email": "ksp11@gmail.com", "userid": "Kishan34", "password": "kp2121"}
        mydict3 = {"fname": "Misita", "lname": "S", "add": "23 Dennet Drive, Toronto", "pin": "M1L5K1",
                   "contact": "+16475232321", "email": "ms@gmail.com", "userid": "Misita21", "password": "misita21"}
        mydict4 = {"fname": "Ayesha", "lname": "Basith", "add": "44 Lupin Drive, Toronto", "pin": "M1K4W2",
                   "contact": "+14165782836", "email": "ayesha33@gmail.com", "userid": "Ayesha33", "password": "aab45"}
        mydict5 = {"fname": "Tarun", "lname": "Dutt", "add": "55 Nugget Ave, Toronto", "pin": "N2K3N1",
                   "contact": "+16477888283", "email": "tdutt44@gmail.com", "userid": "Tarun44", "password": "tdpw44"}
        x = connection_customer.insert_one(mydict)
        x = connection_customer.insert_one(mydict2)
        x = connection_customer.insert_one(mydict3)
        x = connection_customer.insert_one(mydict4)
        x = connection_customer.insert_one(mydict5)
    return render_template('sign_up.html', form=form)



@app.route('/signup1', methods=['GET', 'POST'])
def signup1():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('All fields are required.')
    return render_template('sign_up1.html', form=form)

@app.route('/signup2', methods=['GET', 'POST'])
def signup2():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('All fields are required.')
    return render_template('sign_up2.html', form=form)


@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template("success.html")

@app.route('/cars')
def cars():
    return render_template("cars.html")

if __name__ == '__main__':
    app.run(debug=True)
