//var itensProduto = document.getElementsByTagName('li')
var optionNav = document.getElementsByClassName('retirando')
var optionNav2 = document.getElementsByClassName('excluir')
var usuario = document.getElementsByClassName('user')[0]
console.log(optionNav.length)
console.log(usuario.innerHTML)

for (let i=0; i < optionNav.length; i++){
    text = usuario.innerText
    if ( text === 'ADMIN'){
        optionNav[i].classList.add('hidden');
    }
}

for (let y=0; y < optionNav2.length; y++){
    text = usuario.innerText
    if ( text != 'ADMIN'){
        optionNav2[y].classList.add('hidden');
    }
}
