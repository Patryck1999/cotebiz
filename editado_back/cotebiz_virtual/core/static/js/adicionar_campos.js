var addBtn = document.getElementById("btn");
var idItems = document.getElementById("excluir");
var idItems2 = document.getElementById("marca");
var idItems3 = document.getElementById("unidade-medida");
var idItems4 = document.getElementById("valor-base");
var idItems5 = document.getElementById("dynamic-list");
var contador = 2;


function addItem() {
	//cria a lista com a classe e o estilo
	let item_list_produto = document.createElement("li");
	item_list_produto.classList.add('col-md-12');
	item_list_produto.style.listStyle = "none";
	
	//Cria a lista e o input e Acrescenta o input de produto na lista como um item dela e altera seu estilo
	let produto_list = document.getElementById("produto_list");
	var produtoInput = document.createElement("input");
	produtoInput.classList.add('form-control', 'col-md-12');

	produtoInput.setAttribute('name', 'produto' + contador);
	produtoInput.style.marginBottom = "16px";
	produto_list.appendChild(item_list_produto);
	item_list_produto.appendChild(produtoInput);

	//cria a lista com a classe e o estilo
	let item_list_categoria = document.createElement("li");
	item_list_categoria.classList.add('col-md-12');
	item_list_categoria.style.listStyle = "none";

	//Cria a lista e o input e Acrescenta o input de categoria na lista como um item dela e altera seu estilo
	let categoria_list = document.getElementById("categoria_list");
	let categoriaSelect = document.createElement("select");
	let categoriaOption = document.createElement("option");
	let categoriaOption_1 = document.createElement("option");
	let categoriaOption_2 = document.createElement("option");
	let categoriaOption_3 = document.createElement("option");
	let categoriaOption_4 = document.createElement("option");
	let categoriaOption_5 = document.createElement("option");
	let categoriaOption_6 = document.createElement("option");
	let categoriaOption_7 = document.createElement("option");
	let categoriaOption_8 = document.createElement("option");
	categoriaOption.innerText = '...'
	categoriaOption_1.innerText = 'Material de Limpeza e Higiene'
	categoriaOption_2.innerText = 'Material de Copa'
	categoriaOption_3.innerText = 'Alimentos em Geral'
	categoriaOption_4.innerText = 'Frutas e Verduras'
	categoriaOption_5.innerText = 'Material de Escritório'
	categoriaOption_6.innerText = 'Bebidas'
	categoriaOption_7.innerText = 'Descartáveis e Embalagens'
	categoriaOption_8.innerText = 'Itens de Manutenção Básica'
	categoriaSelect.setAttribute('name', 'categoria' + contador);
	categoriaSelect.style.marginBottom = "16px";
	categoriaSelect.classList.add('form-control', 'col-md-12');
	categoria_list.appendChild(item_list_categoria);
	item_list_categoria.appendChild(categoriaSelect);
	categoriaSelect.appendChild(categoriaOption);
	categoriaSelect.appendChild(categoriaOption_1);
	categoriaSelect.appendChild(categoriaOption_2);
	categoriaSelect.appendChild(categoriaOption_3);
	categoriaSelect.appendChild(categoriaOption_4);
	categoriaSelect.appendChild(categoriaOption_5);
	categoriaSelect.appendChild(categoriaOption_6);
	categoriaSelect.appendChild(categoriaOption_7);
	categoriaSelect.appendChild(categoriaOption_8);


	//cria a lista com a classe e o estilo

	let item_list_valor_base = document.createElement("li");
	item_list_valor_base.classList.add('col-md-12');
	item_list_valor_base.style.listStyle = "none";

	//Cria a lista e o input e Acrescenta o input de valor base na lista como um item dela e altera seu estilo
	let valor_base_list = document.getElementById("valor_base_list");
	let valor_baseInput = document.createElement("input");
	valor_baseInput.setAttribute('name', 'valor_base' + contador);
	valor_baseInput.style.marginBottom = "16px";
	valor_baseInput.classList.add('form-control', 'col-md-12');
	valor_base_list.appendChild(item_list_valor_base);
	item_list_valor_base.appendChild(valor_baseInput);

	//cria a lista com a classe e o estilo
	let item_list_unidade_medida = document.createElement("li");
	item_list_unidade_medida.classList.add('col-md-12');
	item_list_unidade_medida.style.listStyle = "none";

	//Cria a lista e o input e Acrescenta o input de unidade de medida na lista como um item dela e altera seu estilo
	let unidade_medida_list = document.getElementById("unidade_medida_list");
	let unidademedidaSelect = document.createElement("select");
	let unidademedidaOption = document.createElement("option");
	let unidademedidaOption_1 = document.createElement("option");
	let unidademedidaOption_2 = document.createElement("option");
	let unidademedidaOption_3 = document.createElement("option");
	let unidademedidaOption_4 = document.createElement("option");
	let unidademedidaOption_5 = document.createElement("option");
	let unidademedidaOption_6 = document.createElement("option");
	unidademedidaOption.innerText = '...'
	unidademedidaOption_1.innerText = 'Caixa'
	unidademedidaOption_2.innerText = 'Fardo'
	unidademedidaOption_3.innerText = 'Litro'
	unidademedidaOption_4.innerText = 'Pacote'
	unidademedidaOption_5.innerText = 'Unidade'
	unidademedidaOption_6.innerText = 'Par'
	unidademedidaSelect.setAttribute('name', 'unidade_medida' + contador);
	unidademedidaSelect.style.marginBottom = "16px";
	unidademedidaSelect.classList.add('form-control', 'col-md-12');
	unidade_medida_list.appendChild(item_list_unidade_medida);
	item_list_unidade_medida.appendChild(unidademedidaSelect);
	unidademedidaSelect.appendChild(unidademedidaOption);
	unidademedidaSelect.appendChild(unidademedidaOption_1);
	unidademedidaSelect.appendChild(unidademedidaOption_2);
	unidademedidaSelect.appendChild(unidademedidaOption_3);
	unidademedidaSelect.appendChild(unidademedidaOption_4);
	unidademedidaSelect.appendChild(unidademedidaOption_5);
	unidademedidaSelect.appendChild(unidademedidaOption_6);

	//cria a lista com a classe e o estilo
	let item_list_quantidade = document.createElement("li");
	item_list_quantidade.classList.add('col-md-12');
	item_list_quantidade.style.listStyle = "none";

	//Cria a lista e o input e Acrescenta o input de quantidade na lista como um item dela e altera seu estilo
	let quantidade_list = document.getElementById("quantidade_list");
	let qtdInput = document.createElement("input");
	qtdInput.setAttribute('name', 'quantidade' + contador);
	qtdInput.style.marginBottom = "16px";
	qtdInput.classList.add('form-control', 'col-md-12');
	quantidade_list.appendChild(item_list_quantidade);
	item_list_quantidade.appendChild(qtdInput);

	//cria a lista com a classe e o estilo
	let item_list_marca = document.createElement("li");
	item_list_marca.classList.add('col-md-12');
	item_list_marca.style.listStyle = "none";

	//Cria a lista e o input e Acrescenta o input de marca na lista como um item dela e altera seu estilo
	let marca_list = document.getElementById("marca_list");
	let marcaInput = document.createElement("input");
	marcaInput.setAttribute('name', 'marca' + contador);
	marcaInput.style.marginBottom = "16px";
	marcaInput.classList.add('form-control', 'col-md-12');
	marca_list.appendChild(item_list_marca);
	item_list_marca.appendChild(marcaInput);

	//cria a lista com a classe e o estilo
	let item_list_excluir = document.createElement("li");
	item_list_excluir.classList.add('col-md-12');
	item_list_excluir.style.listStyle = "none";

	//Cria a lista e o botao e Acrescenta o botao de exluir na lista como um item dela e altera seu estilo inicia o botao quando ele for clicado
	let excluir_list = document.getElementById("excluir_list");
	var btnDel = document.createElement("button");
	btnDel.setAttribute('name', 'botao' + contador);
	btnDel.classList.add('btn', 'btn-danger');
	btnDel.classList.add('form-control', 'col-md-7');
	btnDel.style.marginBottom = "16px";
	btnDel.appendChild(document.createTextNode("X"));
	excluir_list.appendChild(item_list_excluir);
	item_list_excluir.appendChild(btnDel);
	btnDel.addEventListener("click", deleteListItem);

	//remove o item da lista
	function deleteListItem() {
		item_list_produto.remove();
		item_list_categoria.remove();
		item_list_valor_base.remove();
		item_list_unidade_medida.remove();
		item_list_quantidade.remove();
		item_list_marca.remove();
		item_list_excluir.remove();
	}


}

//pega o valor comprimento total ou seja a quantidade de palavras contidas no campo
function comprimento_do_campo_produto() {
	return produto1.value.length;
}

function comprimento_do_campo_categoria() {
	return categoria1.value.length;
}

function comprimento_do_campo_valor_base() {
	return valor_base1.value.length;
}

function comprimento_do_campo_unidade_medida() {
	return unidade_medida1.value.length;
}

function comprimento_do_campo_quantidade() {
	return quantidade1.value.length;
}

function comprimento_do_campo_marca() {
	return marca1.value.length;
}

// Adiciona o que tiver na função add item de acordo com a condição ao clicar no botao
addBtn.addEventListener('click', function(){
	if((comprimento_do_campo_produto() > 0) && (comprimento_do_campo_categoria() > 0)
	 && (comprimento_do_campo_valor_base() > 0) && (comprimento_do_campo_unidade_medida() > 0) 
	 && (comprimento_do_campo_quantidade() > 0) && (comprimento_do_campo_marca() > 0) 
	 &&  (contador <= 20)){
		addItem();
		contador++;
	  }
});
