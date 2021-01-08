// entry point
function genGeomFunc(product_data) {
	clearAll(); // nsfuncUI3d.js
	init3d(); // nsfuncUI3d.js
	// data table
	let div = document.getElementById('selectors');
	let tbl = document.createElement('table');
	tbl.className = 'datatable';
	let th_name = document.createElement('th');
	th_name.innerHTML = 'Element';
	let th_num = document.createElement('th');
	th_num.innerHTML = 'Faces';
	let th_show = document.createElement('th');
	th_show.innerHTML = 'Show';
	tbl.appendChild(th_name);
	tbl.appendChild(th_num);
	tbl.appendChild(th_show);
	BldgObjLi = [];
	for (var i = 0; i < product_data.length; i++) {
		// make objects from ifc data
		let prod_name = product_data[i].product_name;
		let face_vertex_data = product_data[i].vertices;
		let obj = new bldgObj(
			prod_name,
			prod_name + i.toString(),
			face_vertex_data
		);
		BldgObjLi.push(obj);
		// table for ui
		let tr = updateDataFields(product_data[i], prod_name, i); //below
		tbl.appendChild(tr);
	}
	div.appendChild(tbl); // data-ui
	updateUI(); // below
	render(); // nsfuncUI3d.js
}

function updateDataFields(data, name, i) {
	let tr = document.createElement('tr');
	let td_name = document.createElement('td');
	let td_num = document.createElement('td');
	let td_show = document.createElement('td');
	td_name.innerHTML = data.product_name;
	td_num.innerHTML = data.vertices.length;
	let inp = document.createElement('input');
	inp.type = 'checkbox';
	inp.className = 'showElem';
	inp.id = name + i.toString();
	inp.name = 'showElemSettings';
	td_show.appendChild(inp);
	tr.appendChild(td_name);
	tr.appendChild(td_num);
	tr.appendChild(td_show);
	return tr;
}

function updateUI() {
	var checkboxes = document.querySelectorAll(
		'input[type=checkbox][name=showElemSettings]'
	);
	let selNames = [];
	BldgObjLi.forEach((o) => {
		o.ShowFaces = false;
	});
	checkboxes.forEach(function (checkbox) {
		checkbox.addEventListener('change', function () {
			selNames = Array.from(checkboxes)
				.filter((i) => i.checked)
				.map((i) => i.id);
			//
			let objNames = [];
			selNames.forEach((e) => {
				BldgObjLi.forEach((o) => {
					if (o.Name === e) {
						objNames.push(e);
					}
				});
			});
			//
			for (let i = 0; i < BldgObjLi.length; i++) {
				let t = false;
				for (let j = 0; j < objNames.length; j++) {
					if (objNames[j] === BldgObjLi[i].Name) {
						t = true;
					}
				}
				BldgObjLi[i].ShowFaces = t;
			}
			//
			// console.log(selNames);
			render(); // nsFuncUI3d
		});
	});
}
