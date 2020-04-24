if (localStorage.id_fornecedor) {
	document.getElementById('id_fornecedor').value = localStorage.id_fornecedor;
}
if (localStorage.id_razao_social) {
	document.getElementById('id_razao_social').value = localStorage.id_razao_social;
}
if (localStorage.id_cnpj) {
	document.getElementById('id_cnpj').value = localStorage.id_cnpj;
}
if (localStorage.id_inscricao_estadual) {
	document.getElementById('id_inscricao_estadual').value = localStorage.id_inscricao_estadual;
}
if (localStorage.id_categoria) {
	document.getElementById('id_categoria').value = localStorage.id_categoria;
}
if (localStorage.id_cep) {
	document.getElementById('id_cep').value = localStorage.id_cep;
}
if (localStorage.id_rua) {
	document.getElementById('id_rua').value = localStorage.id_rua;
}
if (localStorage.id_bairro) {
	document.getElementById('id_bairro').value = localStorage.id_bairro;
}
if (localStorage.id_cidade) {
	document.getElementById('id_cidade').value = localStorage.id_cidade;
}
if (localStorage.id_uf) {
	document.getElementById('id_uf').value = localStorage.id_uf;
}
if (localStorage.id_numero) {
	document.getElementById('id_numero').value = localStorage.id_numero;
}
if (localStorage.id_telefone) {
	document.getElementById('id_telefone').value = localStorage.id_telefone;
}
if (localStorage.id_celular) {
	document.getElementById('id_celular').value = localStorage.id_celular;
}
if (localStorage.id_email) {
	document.getElementById('id_email').value = localStorage.id_email;
}
if (localStorage.id_cep) {
	document.getElementById('id_observacao').value = localStorage.id_observacao;
}

var salvarData = function() {
	var id_fornecedor = document.getElementById('id_fornecedor').value;
	var id_razao_social = document.getElementById('id_razao_social').value;
    var id_cnpj = document.getElementById('id_cnpj').value;
	var id_inscricao_estadual = document.getElementById('id_inscricao_estadual').value;
	var id_categoria = document.getElementById('id_categoria').value;
    var id_cep = document.getElementById('id_cep').value;
	var id_rua = document.getElementById('id_rua').value;
	var id_bairro = document.getElementById('id_bairro').value;
	var id_cidade = document.getElementById('id_cidade').value;
	var id_uf = document.getElementById('id_uf').value;
	var id_numero = document.getElementById('id_numero').value;
	var id_telefone = document.getElementById('id_telefone').value;
	var id_celular = document.getElementById('id_celular').value;
	var id_email = document.getElementById('id_email').value;
	var id_observacao = document.getElementById('id_observacao').value;    
	localStorage.setItem('id_fornecedor', id_fornecedor);
	localStorage.setItem('id_razao_social', id_razao_social);
    localStorage.setItem('id_cnpj', id_cnpj);
	localStorage.setItem('id_inscricao_estadual', id_inscricao_estadual);
	localStorage.setItem('id_categoria', id_categoria);
    localStorage.setItem('id_cep', id_cep);
	localStorage.setItem('id_rua', id_rua);
	localStorage.setItem('id_bairro', id_bairro);
	localStorage.setItem('id_cidade', id_cidade);
	localStorage.setItem('id_uf', id_uf);
	localStorage.setItem('id_numero', id_numero);
	localStorage.setItem('id_telefone', id_telefone);
	localStorage.setItem('id_celular', id_celular);
	localStorage.setItem('id_email', id_email);
	localStorage.setItem('id_observacao', id_observacao);   
};
document.onchange = salvarData;