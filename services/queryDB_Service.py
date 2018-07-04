import uuid

from services import root_dir, nice_json
from flask import Flask, request
from werkzeug.exceptions import NotFound
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



@app.route("/deletebyid", methods=['POST'])
def delte_by_id():
    oid = request.form['id']
    db=request.form['db']
    tn=request.form['tn']
    query.delete(db,tn,oid)
    return query.querydatabase(db,tn)

@app.route("/editbyid", methods=['POST'])
def update_by_id():
    oid = request.form['id']
    db=request.form['db']
    tn=request.form['tn']
    record=request.form['record']
    query.update(oid,db,tn,record)
    return query.querydatabasebyID(db,tn,oid)


@app.route("/add_record", methods=['POST'])
def add_record():
    id = str(uuid.uuid4())
    record = request.form['record']# the data that needs to be inserted
    db=request.form['db']
    tn=request.form['tn']
    query.insert(db,tn,[id]+record.split(','))
    return query.querydatabase(db,tn)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
