from flask import Flask,render_template,flash,request,redirect,url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
   

@app.route('/login',methods=["GET","POST"])
def index1():
     if request.method=="POST":
        username = request.args.get("username",'')
        password = request.args.get("password",'')
        try:
            with sqlite3.connect("users.db") as con:
                cur = con.cursor()
                cur.execute("select * from user where username=(?) and password=(?)",(username,password))
                result = cur.fetchone()
                con.commit()
        except:
            return("roll no already exists")        
        
        return  ("login successful")
     return render_template('login.html')


    
    


@app.route('/signup',methods=["GET","POST"])
def index2():
    if (request.method=="POST"):
        rno = request.form.get("rno",'')
        email = request.form.get("email")
        username = request.form.get("username",'')
        password = request.form.get("password",'')
       
        with sqlite3.connect("users.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO user (roll_number,email,username,password) VALUES (?,?,?,?)",(rno,email,username,password) )
                con.commit()
                return render_template('login.html')
       
    return render_template('signup.html')

@app.route('/home')
def index3():
    return render_template('home.html')        

