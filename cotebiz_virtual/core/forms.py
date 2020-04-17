from django import forms
from .models import Fornecedor, Categoria, Email_fornecedor

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