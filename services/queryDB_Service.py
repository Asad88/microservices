import uuid
from flask import Flask, request
import query
app = Flask(__name__)


@app.route("/getall", methods=['POST'])
def get_from_db():
    print("geting data")
    db=request.form['db']
    tn=request.form['tn']
    print("geting data from "+ tn +" in "+ db)
    x= query.querydatabase(db,tn)
    return x


@app.route("/topx", methods=['POST'])
def get_top_db():
    print("geting top 3")
    db=request.form['db']
    tn=request.form['tn']
    print("geting data from "+ tn +" in "+ db)
    x= query.three_max(db , tn)
    return str(x)


@app.route("/getbyid", methods=['POST'])
def get():
    p = request.form['pr']
    db = request.form['db']
    tn = request.form['tn']
    x = query.find(db, tn, p)
    return x


@app.route("/dologin", methods=['POST'])
def login():
    p = request.form['pr']
    db = request.form['db']
    tn = request.form['tn']
    x = query.find(db, tn, p)
    b=len(x)>0
    return str(b)


@app.route("/deletebyid", methods=['POST'])
def delte_by_id():
    oid = request.form['id']
    db=request.form['db']
    tn=request.form['tn']
    print("deleting "+oid + "from "+db)
    query.delete(db,tn,oid)
    return query.querydatabase(db,tn)


# record : c1=v1,c4=v4 ...
@app.route("/editbyid", methods=['POST'])
def update_by_id():
    oid = request.form['id']
    db=request.form['db']
    tn=request.form['tn']
    record=request.form['record']
    print("updating "+oid + "from "+db)
    query.update(oid,db,tn,record)
    return query.querydatabasebyID(db,tn,oid)


@app.route("/add_record", methods=['POST'])
def add_record():
    id = str(uuid.uuid4())
    record = request.form['record']# the data that needs to be inserted
    db = request.form['db']
    tn = request.form['tn']
    x=[id]+record.split(',')
    print(x)
    query.insert(db, tn, x)
    return query.querydatabase(db,tn)



if __name__ == "__main__":
    app.run(port=5000, debug=True)
