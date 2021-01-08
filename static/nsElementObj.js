function Pt(x, y, z) {
	this.x = x;
	this.y = y;
	this.z = z;
}

function bldgObj(type, name, face_vertex_data) {
	this.Type = type;
	this.Name = name;
	this.FaceVertices = face_vertex_data;
	this.ShowFaces = false;
	this.genFaceMesh = () => {
		let meshLi = [];
		for (var j = 0; j < this.FaceVertices.length - 2; j++) {
			let P = this.FaceVertices[j];
			let Q = this.FaceVertices[j + 1];
			let R = this.FaceVertices[j + 2];
			let a = new Pt(P.x, P.y, P.z);
			let b = new Pt(Q.x, Q.y, Q.z);
			let c = new Pt(R.x, R.y, R.z);
			let face = getFace(a, b, c, this.Type); // below
			meshLi.push(face);
		}
		return meshLi;
	};
}

function getFace(a, b, c, name_obj) {
	var geom = new THREE.Geometry();
	geom.vertices.push(a);
	geom.vertices.push(b);
	geom.vertices.push(c);
	geom.vertices.push(a);
	geom.faces.push(new THREE.Face3(0, 1, 2));
	let name = name_obj.toLowerCase();
	let colr = 0xffffff;
	if (name === 'ifcwindow') {
		colr = 0x0000ff;
	} else if (name === 'ifcwall') {
		colr = 0xeeddff;
	} else if (name === 'ifcdoor') {
		colr = 0xffdd00;
	} else if (name === 'ifcslab') {
		colr = 0xdddd00;
	} else if (name === 'ifcwallstandardcase') {
		colr = 0x00eeff;
	}
	var mat = new THREE.MeshBasicMaterial({
		color: colr,
		side: THREE.DoubleSide,
		opacity: 0.75,
		transparent: true,
	});
	var me = new THREE.Mesh(geom, mat);
	return me;
}
