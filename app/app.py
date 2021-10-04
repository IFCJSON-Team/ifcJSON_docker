from flask import Flask

import os
import urllib.request
from flask import Flask, request, redirect, jsonify, send_from_directory, send_file
from werkzeug.utils import secure_filename

import file_converters
import schema_validator

UPLOAD_FOLDER = '/tmp'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def status_message():
    return 'The ifcJSON API is running.'

IFC_EXTENSIONS = {'ifc', 'ifczip', 'ifcxml'}

def allowed_file(filename, extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions

@app.route('/ifc2json', methods=['POST'])
def endpoint_ifc2json():
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message' : 'No file in the request'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename, IFC_EXTENSIONS):
        filename = secure_filename(file.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)
        return jsonify(file_converters.ifc2json(upload_path, request.form.to_dict()))
    else:
        resp = jsonify({'message' : 'Allowed file types are ifc, ifczip, ifcxml'})
        resp.status_code = 400
        return resp
        
@app.route('/json2ifc', methods=['POST'])
def endpoint_json2ifc():
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message' : 'No file in the request'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename, {"json"}):
        filename = secure_filename(file.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)
        out_file = file_converters.json2ifc(upload_path)
        filepath = os.path.split(out_file)
        return send_from_directory(filepath[0], filepath[1], as_attachment=True)
    else:
        resp = jsonify({'message' : 'Allowed file type json'})
        resp.status_code = 400
        return resp
        
@app.route('/validate', methods=['POST'])
def endpoint_validate():
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message' : 'No file in the request'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename, {"json"}):
        filename = secure_filename(file.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)
        resp = jsonify({'message' : schema_validator.json_validate(upload_path)})
        resp.status_code = 200
        return resp
    else:
        resp = jsonify({'message' : 'Allowed file type json'})
        resp.status_code = 400
        return resp

def main():
    app.run(debug=True, host='0.0.0.0', port=3200)

if __name__ == '__main__':
    main()