from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey": "AIzaSyCBY5zkoukL8It9yfn4ZYbE_nLRffPPKAg",
  "authDomain": "cs-group-f-c42f6.firebaseapp.com",
  "projectId": "cs-group-f-c42f6",
  "storageBucket": "cs-group-f-c42f6.appspot.com",
  "messagingSenderId": "121299953984",
  "appId": "1:121299953984:web:f7405100b83a2c6f6532a5",
  "measurementId": "G-L2HVEVYKTJ",
  "databaseURL" : ""
} 
firebase = pyrebase.initialize_app(config)
auth=firebase.auth()





app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = "Authentication failed"
   
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup(): 
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
        login_session['user'] =auth.create_user_with_email_and_password(email, password)
        return redirect(url_for('add_tweet'))
       except:
            error = "Authentication failed"
   


    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


@app.route('/sign_out', methods=['GET', 'POST'])
def sign_out():
    return redirect(url_for('signin'))




if __name__ == '__main__':
    app.run(debug=True)