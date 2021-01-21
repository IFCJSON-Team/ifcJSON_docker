"""
Created on Wed Nov  4 04:41:54 2020

@author: nirviksaha
"""

from flask import Flask, jsonify, render_template, redirect, url_for, request
from flask_cors import CORS
from jan_func import generate_json
from crud import Database
from process_ifc import *
import json


app = Flask(__name__)

CORS(app)

"""
@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message':'hello'})


@app.route('/', methods=['GET'])
def hello2():
    return render_template('index.html')
"""


@app.route('/', methods=['GET'])
def upload():
    db = Database()
    collections = db.get_collections()
    coll_names = []
    for i in collections:
        print(i['name'])
        coll_names.append(i['name'])
    return render_template('ifcFileUpload.html', data=coll_names)


@app.route('/display_file', methods=['GET', 'POST'])
def display_file():
    if request.method == 'POST':
        f = request.files['file']
        chunk = f.stream.read()  # bytes
        s = chunk.decode(encoding='UTF-8')  # string
        if(len(s) == 0):
            return redirect(url_for('upload'))
        with open("tmpIfcFile.ifc", "w") as file:
            file.writelines(s)
        product_li = runExportFuncs()
        return render_template("ifcGenGeom.html", data=product_li)


@app.route('/view_db_entry', methods=['GET', 'POST'])
def view_db_entry():
    filename = request.form['filename']
    print('view entry', filename)
    db = Database()
    r = db.read_records(filename)
    with open("tmpIfcFile.ifc", "w") as file:
        li = r.split("\\n")
        for i in li:
            file.writelines(i)
    product_li = runExportFuncs()
    return render_template("ifcReviewGeo.html", data=product_li)


@app.route('/save_to_db', methods=['GET', 'POST'])
def save_to_db():
    filename = request.form['filename']
    db = Database()
    db.create_records(filename)
    print('save to db', filename)
    return redirect(url_for('upload'))


@app.route('/run_jan_func', methods=["GET", "POST"])
def run_jan_func():
    if request.method == 'POST':
        f = request.files['filename']
        chunk = f.stream.read()
        s = chunk.decode(encoding='UTF-8')
        with open("janIfcFile.ifc", "w") as file:
            file.writelines(s)
        jsonData = json.dumps(generate_json(
            "janIfcFile.ifc", "janJsonFile.json"))
        #  print(json)
        return render_template('run_jsonld.html', data=jsonData)
    else:
        return redirect(url_for('index.html'))


if __name__ == '__main__':
    app.run(debug=True)
