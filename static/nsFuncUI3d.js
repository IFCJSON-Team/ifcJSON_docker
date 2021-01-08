function init3d() {
	scene = new THREE.Scene();
	scene.background = new THREE.Color(0x000000);
	camera = new THREE.PerspectiveCamera(45, Width / Height, 0.01, 1000);
	camera.up = new THREE.Vector3(0, 0, 1);
	camera.position.set(50, 50, 50);
	renderer = new THREE.WebGLRenderer();
	renderer.setSize(Width, Height);
	var div3d = document.getElementById('div3d');
	div3d.appendChild(renderer.domElement);
	controls = new THREE.OrbitControls(camera, renderer.domElement);
	controls.addEventListener('change', render);
	var axis = new THREE.AxesHelper(20);
	scene.add(axis);

	const light = new THREE.PointLight(0xff0000, 1, 100);
	light.position.set(0, 0, 1000);
	scene.add(light);

	render();
}

function update() {
	camera.aspect = Width / Height;
	camera.updateProjectionMatrix();
	renderer.setSize(Width, Height);
}

function render() {
	update();
	clearSceneMesh();
	drawFaces();
	renderer.render(scene, camera);
}

function clearSceneMesh() {
	let errMe = 0;
	meshArr.forEach((me) => {
		try {
			me.geometry.dispose();
			me.material.dispose();
			scene.remove(me);
			delete me;
		} catch (err) {
			errMe++;
		}
	});
	meshArr = [];
	renderer && renderer.renderLists.dispose();
}

function clearAll() {
	var div3d = document.getElementById('div3d');
	while (div3d.children.length > 0) {
		div3d.removeChild(div3d.firstChild);
	}
	let div = document.getElementById('selectors');
	while (div.childNodes.length > 0) {
		div.removeChild(div.firstChild);
	}
}

function drawFaces() {
	BldgObjLi.forEach((o) => {
		if (o.ShowFaces === true) {
			let meLi = o.genFaceMesh();
			meLi.forEach((me) => {
				meshArr.push(me);
			});
		}
	});
	meshArr.forEach((me) => {
		scene.add(me);
	});
}

function showDataFunc() {
	console.clear();
	BldgObjLi.forEach((o) => {
		console.log(o.Name, o.ShowFaces, o.FaceVertices.length);
	});
	console.log('meshes --> ', meshArr.length);
	console.log('scenes --> ', scene.children.length);
}
