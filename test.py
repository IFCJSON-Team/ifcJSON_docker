from flask import Flask, jsonify, render_template, url_for, request
from flask_cors import CORS

import ifcopenshell
import ifcopenshell.geom as geom

app=Flask(__name__)

CORS(app)

@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message':'hello'})


@app.route('/test', methods=['GET'])
def hello2():
    return render_template('index.html')


@app.route('/upload', methods=['GET'])
def upload():
    return render_template('ifcFileUpload.html')


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        chunk = f.stream.read()  # bytes
        s = chunk.decode(encoding='UTF-8')  # string
        with open("tmpIfcFile.ifc", "w") as file:
            file.writelines(s)
        product_li = runExportFuncs()
        return render_template("ifcGenGeom.html", data=product_li)


def procVerts(verts):
    ver = []
    for i in range(0, len(verts)-2, 3):
        p = verts[i]
        q = verts[i + 1]
        r = verts[i + 2]
        ver.append([p, q, r])
    return ver


def procFaces(verts, faces):
    face_triples = []
    for i in range(0, len(faces), 3):
        p = faces[i]
        q = faces[i + 1]
        r = faces[i + 2]
        face_triples.append([p, q, r])
    face_verts = []
    for face in face_triples:
        a = verts[face[0]]
        b = verts[face[1]]
        c = verts[face[2]]
        face_verts.append([a, b, c])
    return face_verts


def runExportFuncs():
    settings = geom.settings()
    settings.set(settings.USE_WORLD_COORDS, True)
    f = ifcopenshell.open("tmpIfcFile.ifc")
    product_li = []
    faces_li = []
    k = 0
    for product in f.by_type("IfcProduct"):
        print(product.is_a())
        all_obj_verts = []
        all_obj_faces = []
        vertex_li = []
        try:
            shape = ifcopenshell.geom.create_shape(settings, product)
            geo = shape.geometry
            obj_verts = procVerts(geo.verts)
            obj_faces = procFaces(obj_verts, geo.faces)
            all_obj_verts.append(obj_verts)
            all_obj_faces.append(obj_faces)
        except Exception as e:
            print('error --> ', e)
        for faces in all_obj_faces:
            for obj in faces:
                for item in obj:
                    vertex = {'x': item[0], 'y': item[1], 'z': item[2]}
                    vertex_li.append(vertex)
                    k += 1
        prod={"product_name": product.is_a(), "vertices": vertex_li}
        product_li.append(prod)
    return product_li


if __name__ == '__main__':
    app.run(debug=True)

