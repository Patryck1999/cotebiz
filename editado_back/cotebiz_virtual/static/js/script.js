var addBtn = document.getElementById("btn");
var idItems = document.getElementById("excluir");
var idItems2 = document.getElementById("marca");
var idItems3 = document.getElementById("unidade-medida");
var idItems4 = document.getElementById("valor-base");
var idItems5 = document.getElementById("dynamic-list");

addBtn.addEventListener('click', function(){
	addClick();
	contador++;
});

function addItemLength() {
	return candidate.value.length;

}

var contador = 1;
	

function addItem() {

	let li1 = document.createElement("li");
	li1.classList.add('col-md-12');
	li1.style.listStyle = "none";

	let div = document.getElementById("dynamic-list");
	var candidate = document.getElementById("candidate");
	var p = document.createElement("p");
	p.classList.add('form-control', 'col-md-12');
	p.setAttribute('id', candidate.value+'_'+contador);
	p.appendChild(document.createTextNode(candidate.value));
	div.appendChild(li1);
	li1.appendChild(p);

	//Cria input para a coluna de Valor Base
	
	let li2 = document.createElement("li");
	li2.style.listStyle = "none";

	let categoriaId = document.getElementById("categoria");
	let categoriaInput = document.createElement("input");
	categoriaInput.setAttribute('id', 'categoria' + contador);
	categoriaInput.style.marginBottom = "16px";
	categoriaInput.classList.add('form-control', 'col-md-12');
	categoriaId.appendChild(li2);
	li2.appendChild(categoriaInput);


	//Cria input para a coluna de Valor Base

	let li3 = document.createElement("li");
	li3.style.listStyle = "none";

	let vl = document.getElementById("valor-base");
	let valorbase = document.createElement("input");
	valorbase.setAttribute('id', 'valorbase' + contador);
	valorbase.style.marginBottom = "16px";
	valorbase.classList.add('form-control', 'col-md-12');
	vl.appendChild(li3);
	li3.appendChild(valorbase);

	//Cria input para a coluna de Unidade Medida

	let li4 = document.createElement("li");
	li4.style.listStyle = "none";

	let um = document.getElementById("unidade-medida");
	let unidademedida = document.createElement("input");
	unidademedida.setAttribute('id', 'nome' + contador);
	unidademedida.style.marginBottom = "16px";
	unidademedida.classList.add('form-control', 'col-md-12');
	um.appendChild(li4);
	li4.appendChild(unidademedida);

	//Cria input para a coluna de Marca

	let li5 = document.createElement("li");
	li5.style.listStyle = "none";

	let ma = document.getElementById("marca");
	let marca = document.createElement("input");
	marca.setAttribute('id', 'marca' + contador);
	marca.style.marginBottom = "16px";
	marca.classList.add('form-control', 'col-md-12');
	ma.appendChild(li5);
	li5.appendChild(marca);

	//Cria input para a coluna de Marca

	let li6 = document.createElement("li");
	li6.style.listStyle = "none";
	li6.setAttribute('id', 'ex'+contador);
	let ixi = document.getElementsByTagName("li")[0];

	let btn = document.getElementById("excluir");
	var btnDel = document.createElement("button");
	btnDel.setAttribute('id', 'botao' + contador);
	btnDel.classList.add('btn', 'btn-danger');
	btnDel.style.marginBottom = "16px";
	btnDel.appendChild(document.createTextNode("X"));
	btn.appendChild(li6);
	li6.appendChild(btnDel);
	btnDel.addEventListener("click", deleteListItem);

	candidate.value = "";
	
	function deleteListItem() {
		btn.parent.removeChild(ixi);
	}
	
	
}


function addClick() {
	if(addItemLength() > 0) {
	  addItem();
	}
}
  
  // On keypress enter
/*function addKey(event) {
	if(addItemLength() > 0 && event.keyCode == 13) {
		addItem();
	}
}*/