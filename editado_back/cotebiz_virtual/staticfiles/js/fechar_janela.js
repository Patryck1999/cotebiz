function fechar_janela(){
    var categoria = document.getElementById("id_categoria").value;
        if (categoria != '') {
            window.opener = window
            window.close("#")
        }
}