from werkzeug.utils import redirect
from flask import Flask, request, render_template, url_for, flash, session
import os, datetime
from werkzeug.exceptions import NotFound, ServiceUnavailable
import json
import query ,json
import requests


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/", methods=['GET'])
def root():
    return render_template("user_main.html")


@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        record = str({request.form['uname'], datetime.datetime.now().strftime("%Y-%m-%d %H:%M") ,request.form['pass']})
        data = {'db': "database.db", 'tn': "users", 'record': record}
        print("posting :" + str(data))
        try:
            r = requests.post("http://127.0.0.1:5000/add_record", data=data)
        except requests.exceptions.ConnectionError:
            raise ServiceUnavailable("The Movie service is unavailable.")
        return r.text

    return render_template("signup.html")


@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        p = " names = '"+request.form['uname']+"' and pass = '"+request.form['pass']+"'"
        data = {'db': request.form['db'], 'tn': request.form['tn'],'pr': p}
        print(data)
        try:
            r = requests.post("http://127.0.0.1:5000/dologin",data=data)
            print(r.text)
            if r.text == str(True):
                session['uname'] = request.form['uname']
                return redirect(url_for('save'))
            else:
                return "wrong credintials"
        except requests.exceptions.ConnectionError:
            raise ServiceUnavailable("The Movie service is unavailable.")
    return render_template("login.html")


@app.route("/list_movies", methods=['GET'])
def list_movies():
    if session is None:
        return "set up DB firt. go to /logeduser/"
    try:
        data = {'db': session['db'], 'tn': session['tn']}
        r = requests.post("http://127.0.0.1:5001/movielist", data=data)
    except requests.exceptions.ConnectionError:
        raise ServiceUnavailable("The Movie service is unavailable.")
    return r.text


@app.route("/top3/", methods=['GET'])
def top3():
    if session is None:
        return "set up DB first. go to /logeduser/"
    try:
        data = {'db': session['db'], 'tn': 'movies'}
        r = requests.post("http://127.0.0.1:5000/topx", data=data)
    except requests.exceptions.ConnectionError:
        raise ServiceUnavailable("The Movie service is unavailable.")
    return r.text


@app.route("/logeduser/", methods=['GET','POST'])
def save():
    if request.method =='POST':
        session['db'] = request.form['db']
        session['tn'] = request.form['tn']
        return render_template("redyuser.html")
    return render_template("logeduser.html")



@app.route("/order", methods=['GET', 'POST'])
def order_movie():
    if request.method == 'POST':
        if session is None:
            return "set up DB firt. go to /logeduser/"
        try:
            record = str({'mid': request.form['mid'], 'uid': session['uname'], 'date': request.form['date']})
            data = {'db': request.form['db'], 'tn': request.form['tn'],'record': record }
            r = requests.post("http://127.0.0.1:5000/add_record", data=data)
        except requests.exceptions.ConnectionError:
            raise ServiceUnavailable("The Movie service is unavailable.")
        return r.text

    return render_template('ordermovie.html')


if __name__ == "__main__":
    app.run(port=5002, debug=True)
