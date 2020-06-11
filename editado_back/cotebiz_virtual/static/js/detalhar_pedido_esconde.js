var itensProduto = document.getElementsByClassName('controle')
console.log(itensProduto.length)
console.log(itensProduto.innerText)
for (let i=0; i < itensProduto.length; i++){
    let texto = itensProduto[i].innerText;  
    if ( texto === 'None'){
        itensProduto[i].classList.add('hidden');  
    }
    console.log(texto)
}