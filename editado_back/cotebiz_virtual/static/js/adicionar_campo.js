$( "#add-campo" ).click(function() {
    $( "#div-produto" ).append('<select name="produto"><option value="">Selecione um item</option>{% for produto in produtos %}<option value="{{produto.id}}" name="titulo[]" placeholder="Produto">{{produto}}</option>{% endfor %}</select>');
    $( "#div-quantidade" ).append('<input name="titulo[]" placeholder="Quantidade" id="quantidade" type="number">');
  });