from django.contrib import admin
from .models import Fornecedor, Categoria, Email_fornecedor, Email_fornecedor_envio, Cliente, Email_cliente, Produto, Pedido_de_cotacao,Pedido_de_cotacao_clone, Pedido_de_cotacao_fornecedor
# Register your models here.
@admin.register(Fornecedor)
class Fornecedoradmin(admin.ModelAdmin):
    list_display = ['id', 'fornecedor', 'cnpj', 'inscricao_estadual', 'cidade']

@admin.register(Categoria)
class Categoriaadmin(admin.ModelAdmin):
     list_display = ['id', 'categoria']

@admin.register(Email_fornecedor)
class Email_fornecedoradmin(admin.ModelAdmin):
     list_display = ['id', 'email']

@admin.register(Email_fornecedor_envio)
class Email_fornecedor_envioadmin(admin.ModelAdmin):
     list_display = ['id', 'email']

@admin.register(Cliente)
class Clienteadmin(admin.ModelAdmin):
     list_display = ['id', 'cliente', 'plano', 'cpf', 'rua', 'numero', 'bairro', 'email'] 
@admin.register(Email_cliente)
class Email_clienteadmin(admin.ModelAdmin):
     list_display = ['id', 'email']

@admin.register(Produto)
class Produtoadmin(admin.ModelAdmin):
     list_display = ['id', 'produto', 'categoria', 'unidade_medida', 'marca']

@admin.register(Pedido_de_cotacao)
class Pedido_de_cotacaoadmin(admin.ModelAdmin):
     list_display = ['id', 'nome', 'razao_social', 'cnpj', 'plano', 'cep','rua', 'bairro', 'cidade',
      'numero', 'telefone', 'celular']

@admin.register(Pedido_de_cotacao_clone)
class Pedido_de_cotacao_clonedmin(admin.ModelAdmin):
     list_display = ['id', 'nome', 'razao_social', 'cnpj', 'plano', 'cep','rua', 'bairro', 'cidade',
      'numero', 'telefone', 'celular']

@admin.register(Pedido_de_cotacao_fornecedor)
class Pedido_de_cotacaoadmin(admin.ModelAdmin):
     list_display = ['id', 'observacao_1']