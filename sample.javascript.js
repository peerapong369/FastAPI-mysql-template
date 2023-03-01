async function deleteRow(id) {
	var url = "http://192.168.16.140:8004/ngrstockmaster/" + id;
	//console.log(url);
	const response = await fetch(url, {
		method: 'DELETE',
		headers: { 'accept': 'application/json' }
	});
	const result = await response.json();
	//console.log(result.detail);

	location.reload();
}

async function updateRow(id) {
	var url = "http://192.168.16.140:8004/ngrstockmaster/" + id;
	//console.log(url);

	var data = { "locker": "String", "product_name": "String", "type": "String", "qlimit": 0 };

	var locker = document.getElementById("inputtdlocker_" + id).value;
	var product = document.getElementById("inputtdpd_" + id).value;
	var type = document.getElementById("selecttdtype_" + id).value;
	var glimit = document.getElementById("inputtdlimit_" + id).value;

	data.locker = locker;
	data.product_name = product;
	data.type = type;
	data.qlimit = parseInt(glimit);



	const response = await fetch(url, {
		method: 'PUT',
		headers: { 'accept': 'application/json', 'Content-Type': 'application/json' },
		body: JSON.stringify(data),
	});
	const result = await response.json();
	console.log(result);

	location.reload();
}

async function insertRow(id) {
	var url = "http://192.168.16.140:8004/ngrstockmaster/";
	//console.log(url);

	var data = { "locker": "String", "product_name": "String", "type": "String", "qlimit": 0 };

	var locker = document.getElementById("inputtdlocker_0").value;
	var product = document.getElementById("inputtdpd_0").value;
	var type = document.getElementById("selecttdtype_0").value;
	var glimit = document.getElementById("inputtdlimit_0").value;

	data.locker = locker;
	data.product_name = product;
	data.type = type;
	data.qlimit = parseInt(glimit);



	const response = await fetch(url, {
		method: 'POST',
		headers: { 'accept': 'application/json', 'Content-Type': 'application/json' },
		body: JSON.stringify(data),
	});
	const result = await response.json();
	console.log(result);

	location.reload();
}