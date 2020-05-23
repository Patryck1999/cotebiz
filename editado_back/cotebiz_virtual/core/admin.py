from django.contrib import admin
from .models import Fornecedor, Categoria, Email_fornecedor, Cliente, Email_cliente, Produto
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

@admin.register(Cliente)
class Clienteadmin(admin.ModelAdmin):
     list_display = ['id', 'cliente', 'plano', 'cpf', 'rua', 'numero', 'bairro', 'email'] 
@admin.register(Email_cliente)
class Email_clienteadmin(admin.ModelAdmin):
     list_display = ['id', 'email']

@admin.register(Produto)
class Produtoadmin(admin.ModelAdmin):
     list_display = ['id', 'produto', 'categoria', 'unidade_medida', 'marca']