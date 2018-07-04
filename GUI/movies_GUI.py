import requests,os

from services import root_dir, nice_json
from flask import Flask, request,render_template,redirect,session
from werkzeug.exceptions import NotFound
import query
app = Flask(__name__)

@app.route("/", methods=['GET'])
def root():
    return render_template("moves_main.html")

@app.route("/movielist", methods=['GET','POST'])
def movie_list():
    if request.method == 'POST':
        r = requests.get("http://127.0.0.1:5000/getall")
        print(r.status_code, r.reason)
        return r.text
    return render_template("post_req_for_ml.html")


@app.route("/addmovie", methods=['GET','POST'])
def add_movie():
    if request.method == 'POST':
        record=str({request.form['title'],request.form['director'],request.form['rating']})
        data={'db': request.form['db'],'tn': request.form['tn'], 'record':record}
        print(data)
        r = requests.post("http://127.0.0.1:5000/add_record", data=data)
        print(r.status_code, r.reason)
        return r.text
    return render_template("addmovie.html")


@app.route("/movie_remove", methods=['GET','POST'])
def movie_remove():
    if request.method == 'POST':
        record=request.form('mid')
        data={'db': request.form['db'],'tn': request.form['tn'], 'record':record}
        print(data)
        r = requests.post("http://127.0.0.1:5000/deletebyid", data=data)
        print(r.status_code, r.reason)
        return r.text
    return render_template("removmovie.html")


if __name__ == "__main__":
    app.run(port=5002, debug=True)
