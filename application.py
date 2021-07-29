from flask import Flask, render_template, request,session,redirect,url_for

import os
from models import *
from datetime import datetime

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db.init_app(app)

with app.app_context():
    db.create_all()




@app.route("/register",methods=['GET','POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:

        name=request.form.get("Username")
        email=request.form.get("Gmail")
        pwd=request.form.get("Password")
    
        f=Register(name=name,mail=email,password=pwd)
        db.session.add(f)
        db.session.commit()

        

        return f"Username {name} is registered."

@app.route("/auth",methods=['GET','POST'])
def authorize():
    if 'name' in session:
        name=session['name']
        return "Logged in as " +name + "<a href='/logout'>Click here to logout</a>"

    return "User is not logged in <a href='/login'>click here to login</a>"

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        session['name']=request.form['name']
        return redirect(url_for('register'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('name',None)
    return redirect(url_for('register'))
