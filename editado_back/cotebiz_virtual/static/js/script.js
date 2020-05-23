var addBtn = document.getElementById("btn");
var divItems = document.getElementsByClassName("remove");

addBtn.addEventListener('click', addClick);
addBtn.addEventListener('click', removeItem);

function addItemLength() {
	return document.getElementById("candidate").value.length;
}

function addItem() {
	let div = document.getElementById("dynamic-list");
	var candidate = document.getElementById("candidate");
	var p = document.createElement("p");
	p.classList.add('form-control', 'col-md-12');
	p.setAttribute('id', candidate.value);
	p.appendChild(document.createTextNode(candidate.value));
	div.appendChild(p);
	candidate.value = "";
}

function addValorBase(){
	var div = document.getElementById("valor-base");
	var valorbase = document.createElement("input");
	valorbase.style.marginBottom = "16px";
	valorbase.classList.add('form-control', 'col-md-12');
	return div.appendChild(valorbase);
}
	
function addUnidadeMedida(){
	let div = document.getElementById("unidade-medida");
	let select = document.createElement("select");
	let cartela  = document.createElement("option");
	let caixa  = document.createElement("option");
	let duzia  = document.createElement("option");
	let pacote  = document.createElement("option");
	cartela.innerHTML = "cartela";
	caixa.innerHTML = "caixa";
	duzia.innerHTML = "duzia";
	pacote.innerHTML = "pacote";
	select.style.marginBottom = "16px";
	select.classList.add('form-control', 'col-md-12');
	div.appendChild(select);
	select.appendChild(cartela);
	select.appendChild(caixa);
	select.appendChild(duzia);
	select.appendChild(pacote);
}
	
function addMarca(){
	let div = document.getElementById("marca");
	let marca = document.createElement("input");
	marca.style.marginBottom = "16px";
	marca.classList.add('form-control', 'col-md-12');
	div.appendChild(marca);
}

function buttonDelete(){
	let div = document.getElementById("excluir");
	let btnDel = document.createElement("button");
	btnDel.classList.add('btn', 'btn-danger');
	btnDel.appendChild(document.createTextNode("X"));
	div.appendChild(btnDel);
	btnDel.addEventListener("click", deleteListItem);
}

function deleteListItem() {
	removeChild(divItems);
}

function removeItem() {
	var ul = document.getElementById("dynamic-list");
	var candidate = document.getElementById("candidate");
	var item = document.getElementById(candidate.value);
	ul.removeChild(item);
}


function addClick() {
	if(addItemLength() > 0) {
	  addItem();
	  addValorBase();
	  addUnidadeMedida();
	  addMarca();
	  buttonDelete();
	  deleteListItem();
	}
  }
  
  // On keypress enter
  function addKey(event) {
	if(addItemLength() > 0 && event.keyCode == 13) {
		addItem();
	}
  }
  
  
  input.addEventListener('keypress', addKey);
  