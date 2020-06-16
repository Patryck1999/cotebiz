from django import forms
from .models import *

class FornecedorForm(forms.ModelForm):
    fornecedor = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', }),required=True, max_length=100)
    razao_social = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', }),required=True, max_length=100)
    cnpj = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', }),required=True, max_length=100)
    inscricao_estadual = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', }),required=False, max_length=100)
    categoria = forms.Select(attrs={'class':'form-control'})
    cep = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True, max_length=100)
    rua = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True, max_length=100)
    bairro = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True, max_length=100)
    cidade = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True, max_length=100)
    uf = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True, max_length=100)
    numero = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True, max_length=100)
    telefone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False, max_length=100)
    celular = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False, max_length=100)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', }),required=True, max_length=250)
    observacao = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), max_length=100, required=False)
    class Meta:
        model = Fornecedor
        fields = ['fornecedor', 'razao_social', 'cnpj', 'inscricao_estadual', 'categoria','cep', 'rua',
                  'bairro', 'cidade', 'uf', 'numero', 'telefone', 'celular', 'email', 'observacao']
