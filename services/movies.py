import requests
from flask import Flask, request,render_template
from werkzeug.exceptions import ServiceUnavailable
app = Flask(__name__)


@app.route("/", methods=['GET'])
def root():
    return render_template("moves_main.html")


@app.route("/movielist", methods=['GET','POST'])
def movie_list():
    if request.method == 'POST':
        data = {'db': request.form['db'], 'tn': request.form['tn']}
        print("posting :" + str(data))
        try:
            r = requests.post("http://127.0.0.1:5000/getall",data=data)
        except requests.exceptions.ConnectionError:
            raise ServiceUnavailable("The Movie service is unavailable.")
        return r.text
    return render_template("post_req_for_ml.html")


@app.route("/add_movie", methods=['GET','POST'])
def add_movie():
    if request.method == 'POST':
        record = str({request.form['title'],request.form['director'],request.form['rating']})
        data = {'db': request.form['db'],'tn': request.form['tn'], 'record': record}
        print("posting :" +str(data) )
        try:
            r = requests.post("http://127.0.0.1:5000/add_record", data=data)
        except requests.exceptions.ConnectionError:
            raise ServiceUnavailable("The Movie service is unavailable.")
        return r.text
    return render_template("addmovie.html")


@app.route("/movie_remove", methods=['GET','POST'])
def movie_remove():
    if request.method == 'POST':
        record = request.form['mid']
        data = {'db': request.form['db'], 'tn': request.form['tn'], 'id': record}
        print("posting :" + str(data))
        try:
            r = requests.post("http://127.0.0.1:5000/deletebyid", data=data)
        except requests.exceptions.ConnectionError:
            raise ServiceUnavailable("The Movie service is unavailable.")
        return r.text
    return render_template("removmovie.html")


@app.route("/movie_update", methods=['GET','POST'])
def movie_update():
    if request.method == 'POST':
        mid = request.form['mid']
        rating = request.form['rating']
        record = "rating = "+rating
        data = {'db': request.form['db'], 'tn': request.form['tn'], 'id': mid, 'record': record}
        print("posting :" + str(data))
        try:
            r = requests.post("http://127.0.0.1:5000/editbyid", data=data)
        except requests.exceptions.ConnectionError:
            raise ServiceUnavailable("The Movie service is unavailable.")
        return r.text
    return render_template("editmovie.html")


@app.route("/ordermovie", methods=['POST'])
def ordermovie():
    record = str({request.form['mid'],request.form['uid'], request.form['date']})
    data = {'db': request.form['db'], 'tn': request.form['tn'], 'record': record}
    try:
        print(data)
        r = requests.post("http://127.0.0.1:5000/add_record", data=data)
        print(r.reason)
    except requests.exceptions.ConnectionError:
        raise ServiceUnavailable("The Movie service is unavailable.")
    return r.text


if __name__ == "__main__":
    app.run(port=5001, debug=True)
