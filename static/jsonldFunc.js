function showJson() {
	let taData = document.getElementById('interactiveTAData');
	prettyPrint(taData, jsonData);
}

function showJsonLD() {
	let taData = document.getElementById('interactiveTAData');
	prettyPrint(taData, jsonLdContext);
}

function showFramedView() {
	console.log('framed view');
}

function prettyPrint(ta, res) {
	try {
		var pretty = JSON.stringify(res, undefined, 4);
		ta.value = pretty;
	} catch (err) {
		console.log(err);
		ta.value = JSON.stringify(res);
	}
}

async function genFrame() {
	console.log('generate solutions');
	let data = JSON.parse(document.getElementById('interactiveTAData').value);
	let frame = JSON.parse(document.getElementById('interactiveTAFrame').value);
	console.log(typeof data);
	console.log(typeof frame);

	try {
		let framedData = await jsonld.frame(data, frame);
		let ta = document.getElementById('outputTAFrame');
		prettyPrint(ta, framedData);
		let div = document.getElementById('floatingOutputPanel');
		div.style.display = 'block';
	} catch (e) {
		// console.log(e);
	}
}

function hideOutput() {
	let ta = document.getElementById('floatingOutputPanel');
	ta.style.display = 'none';
}
