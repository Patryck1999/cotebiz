from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField('Categoria', max_length=20, unique=True)

    class Meta:
        verbose_name ='Categoria'
        verbose_name_plural ='Categorias'
        

    def __str__(self):
        return str(self.categoria)


class Email_fornecedor(models.Model):
    email = models.EmailField('email', max_length=100, unique=True)
    class Meta:
        verbose_name ='Email_Fornecedor'
        verbose_name_plural ='Email_Fornecedores'
        

    def __str__(self):
        return str(self.email)   

class Fornecedor(models.Model):
    fornecedor = models.CharField('Fornecedores', max_length=80, unique=True)
    razao_social = models.CharField('Razão Social.', max_length=40)
    cnpj = models.CharField('CNPJ',max_length=18)
    inscricao_estadual = models.CharField('I.Estadual:',max_length=15)
    categoria_choices = (
                ('Material de Limpeza e Higiene','Material de Limpeza e Higiene'),
                ('Material de Copa','Material de Copa'),
                ('Alimentos em Geral', 'Alimentos em Geral'),
                ('Frutas e Verduras', 'Frutas e Verduras'),
                ('Material de Escritório', 'Material de Escritório'),
                ('Bebidas', 'Bebidas'),
                ('Descartáveis e Embalagens', 'Descartáveis e Embalagens'),
                ('Itens de Manutenção Básica', 'Itens de Manutenção Básica'),
    )
    categoria = models.CharField(max_length=100, choices=categoria_choices)
    cep = models.CharField('CEP', max_length=11)
    rua = models.CharField('Rua', max_length=100)
    bairro = models.CharField('Bairro', max_length=30)
    cidade = models.CharField('Cidade', max_length=30)
    uf = models.CharField('UF', max_length=30)
    numero = models.CharField('Número', max_length=10)
    telefone = models.CharField('Telefone', max_length=16, null=True, blank=True)
    celular = models.CharField('Celular', max_length=17, null=True, blank=True)
    email = models.ForeignKey(Email_fornecedor, on_delete=models.CASCADE)
    observacao = models.CharField('Observação', max_length=400, null=True, blank=True)

    class Meta:
        verbose_name ='Fornecedor'
        verbose_name_plural ='Fornecedores'

    def __str__(self):
        return str(self.fornecedor)


class Produto(models.Model):
    produto = models.CharField('Produto', max_length=20)
    valor_base = models.CharField('Valor Base', max_length=20)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    unidade_medida = models.CharField('Unidade de Medida', max_length=2)
    marca = models.CharField('Marca', max_length=20)

    class Meta:
        verbose_name ='Produto'
        verbose_name_plural ='Produtos'
        

    def __str__(self):
        return str(self.produto)


class Email_cliente(models.Model):
    email = models.EmailField('email', unique=True)
    class Meta:
        verbose_name ='Email_Cliente'
        verbose_name_plural ='Email_Clientes'
        

    def __str__(self):
        return str(self.email)   
        

class Cliente(models.Model):
    cliente = models.CharField('Cliente', max_length=80)
    plano = models.CharField('Plano', max_length=20)
    cpf = models.CharField('CPF', max_length=14)
    rua = models.CharField('Rua', max_length=100)
    numero = models.CharField('Número', max_length=10)
    bairro = models.CharField('Bairro', max_length=40)
    email = models.ForeignKey(Email_cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name ='Cliente'
        verbose_name_plural ='Clientes'
        

    def __str__(self):
        return str(self.cliente)

     
class Pedido_de_cotacao(models.Model):
    pedido_de_cotacao = models.CharField('Pedido', max_length=20)
    quantidade = models.CharField('quantidade', max_length=5)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name ='Pedido_de_cotacao'
        verbose_name_plural ='Pedidos_de_cotacao'


    def __str__(self):
        return str(self.pedido_de_cotacao)   

    
class Sala_de_leilao(models.Model):
    pedido = models.ForeignKey(Pedido_de_cotacao, on_delete=models.CASCADE)

    class Meta:
        verbose_name ='Sala_de_leilao'
        verbose_name_plural ='Salas_de_leilao'
        

    def __str__(self):
        return str(self.pedido)   