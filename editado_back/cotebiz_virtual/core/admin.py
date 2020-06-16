from django.contrib import admin
from .models import Fornecedor, Pedido_de_cotacao, Pedido_de_cotacao_clone, Pedido_de_cotacao_fornecedor
# Register your models here.
@admin.register(Fornecedor)
class Fornecedoradmin(admin.ModelAdmin):
    list_display = ['id', 'fornecedor', 'cnpj', 'inscricao_estadual', 'cidade']

@admin.register(Pedido_de_cotacao)
class Pedido_de_cotacaoadmin(admin.ModelAdmin):
     list_display = ['id', 'nome', 'razao_social', 'cnpj', 'plano', 'cep','rua', 'bairro', 'cidade',
      'numero', 'telefone', 'celular']

@admin.register(Pedido_de_cotacao_clone)
class Pedido_de_cotacao_clonedmin(admin.ModelAdmin):
     list_display = ['id', 'nome', 'razao_social', 'cnpj', 'plano', 'cep','rua', 'bairro', 'cidade',
      'numero', 'telefone', 'celular']

@admin.register(Pedido_de_cotacao_fornecedor)
class Pedido_de_cotacao_fornecedoradmin(admin.ModelAdmin):
     list_display = ['id', 'fornecedor']