from flask import Flask,render_template,flash,request,redirect,url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisthekey'




    

            

class User(db.Model, UserMixin):
    email = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(20), nullable=False, )
    password = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    return render_template("index.html")
   
@app.route('/login',methods=["GET","POST"])
def index1():
     
     if request.method=="POST":
         email = request.form['log-email']
         password = request.form['log-password']
         user = User.query.filter_by(email=email).first()
         if user:
            if (user.password == password):
                
                return ("succesfully logged")
         
     return render_template('index.html')


@app.route('/register',methods=["GET","POST"])
def index2():
     

    if request.method=="POST":
     try:
         name = request.form['reg-name']
         email = request.form['reg-email']
         password = request.form['reg-password']
         existing_user_email = User.query.filter_by( email=email).first()
         if existing_user_email:
            raise ValidationError(
                'That username already exists. Please choose a different one.')
         new_user = User(name=name,email=email,password=password)
         db.session.add(new_user)
         db.session.commit()
         return render_template('index.html')
     except:
             
             return('That username already exists. Please choose a different one.')
        
    return render_template('index.html')     
