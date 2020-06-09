var itensProduto = document.getElementsByTagName('li')
var clicaItensProduto = document.getElementsByClassName('retirar')
console.log(itensProduto.innerHTML)
for (let i=0; i < itensProduto.length; i++){
    let texto = itensProduto[i].innerHTML;
    if ( texto === 'None'){
        clicaItensProduto[i].classList.add('hidden');
    }
}
