from django import forms
from .models import Fornecedor, Categoria, Email_fornecedor, Pedido_de_cotacao

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['fornecedor', 'razao_social', 'cnpj', 'inscricao_estadual', 'categoria','cep', 'rua',
                  'bairro', 'cidade', 'uf', 'numero', 'telefone', 'celular', 'email', 'observacao']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria']

class Email_fornecedorForm(forms.ModelForm):
    class Meta:
        model = Email_fornecedor
        fields = ['email']

class Pedido_de_cotacaoForm(forms.ModelForm):
    class Meta:
        model = Pedido_de_cotacao
        fields = ['pedido_de_cotacao', 'quantidade', 'produto', 'cliente', 'categoria'] 
