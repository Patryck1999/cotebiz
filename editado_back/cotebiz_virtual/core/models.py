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

class Email_fornecedor_envio(models.Model):
    email = models.ForeignKey(Email_fornecedor, on_delete=models.CASCADE)
    class Meta:
        verbose_name ='Email_fornecedor_envio'
        verbose_name_plural ='Email_fornecedor_envio'
        

    def __str__(self):
        return str(self.email)   

class Fornecedor(models.Model):
    fornecedor = models.CharField('Nome Fantasia', max_length=40, unique=True)
    razao_social = models.CharField('Razão Social.', max_length=80)
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
    email = models.CharField('Email', max_length=150, null=True, blank=True)
    observacao = models.CharField('Observação', max_length=400, null=True, blank=True)

    class Meta:
        verbose_name ='Fornecedor'
        verbose_name_plural ='Fornecedores'

    def __str__(self):
        return str(self.fornecedor)


class Produto(models.Model):
    produto = models.CharField('Produto', max_length=20)
    valor_base = models.CharField('Valor Base', max_length=20)
    categoria = models.CharField('Categoria', max_length=20)
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
    email = models.CharField('Email', max_length=40)

    class Meta:
        verbose_name ='Cliente'
        verbose_name_plural ='Clientes'
        

    def __str__(self):
        return str(self.cliente)

     
class Pedido_de_cotacao(models.Model):
    data_agora = models.DateTimeField()
    nome = models.CharField('Nome Fantasia', max_length=40)
    razao_social = models.CharField('Razão Social', max_length=80)
    cnpj = models.CharField('CNPJ', max_length=18)
    plano = models.CharField('Tipo do Plano', max_length=1)
    cep = models.CharField('CEP', max_length=11)
    rua = models.CharField('Rua', max_length=100)
    bairro = models.CharField('Bairro', max_length=30)
    cidade = models.CharField('Cidade', max_length=30)
    numero = models.CharField('Número', max_length=10)
    telefone = models.CharField('Telefone', max_length=16)
    celular = models.CharField('Celular', max_length=17)
    email = models.CharField('Email', max_length=150)

    produto1 = models.CharField('Produto 1', max_length=25)
    categoria1 = models.CharField('Categoria 1', max_length=100)
    valor_base1 = models.CharField('Valor Base 1', max_length=9)
    unidade_medida1 = models.CharField('Unidade de Medida 1', max_length=9)
    quantidade1 = models.CharField('Quantidade 1', max_length=5)
    marca1 = models.CharField('Marca 1', max_length=9)
    

    produto2 = models.CharField('Produto 2', max_length=25, null=True, blank=True)
    categoria2 = models.CharField('Categoria 2', max_length=100, null=True, blank=True)
    valor_base2 = models.CharField('Valor Base 2', max_length=9, null=True, blank=True)
    unidade_medida2 = models.CharField('Unidade de Medida 2', max_length=9, null=True, blank=True)
    quantidade2 = models.CharField('Quantidade 2', max_length=5, null=True, blank=True)
    marca2 = models.CharField('Marca 2', max_length=9, null=True, blank=True)


    produto3 = models.CharField('Produto 3 ', max_length=25, null=True, blank=True)
    categoria3 = models.CharField('Categoria 3', max_length=100, null=True, blank=True)
    valor_base3 = models.CharField('Valor Base 3', max_length=9, null=True, blank=True)
    unidade_medida3 = models.CharField('Unidade de Medida 3', max_length=9, null=True, blank=True)
    quantidade3 = models.CharField('Quantidade 3', max_length=5, null=True, blank=True)
    marca3 = models.CharField('Marca 3', max_length=9, null=True, blank=True)


    
    produto4 = models.CharField('Produto 4', max_length=25, null=True, blank=True)
    categoria4 = models.CharField('Categoria 4', max_length=100, null=True, blank=True)
    valor_base4 = models.CharField('Valor Base 4', max_length=9, null=True, blank=True)
    unidade_medida4 = models.CharField('Unidade de Medida 4', max_length=9, null=True, blank=True)
    quantidade4 = models.CharField('Quantidade 4', max_length=5, null=True, blank=True)
    marca4 = models.CharField('Marca 4', max_length=9, null=True, blank=True)


    produto5 = models.CharField('Produto 5', max_length=25, null=True, blank=True)
    categoria5 = models.CharField('Categoria 5', max_length=100, null=True, blank=True)
    valor_base5 = models.CharField('Valor Base 5', max_length=9, null=True, blank=True)
    unidade_medida5 = models.CharField('Unidade de Medida 5', max_length=9, null=True, blank=True)
    quantidade5 = models.CharField('Quantidade 5', max_length=5, null=True, blank=True)
    marca5 = models.CharField('Marca 5', max_length=9, null=True, blank=True)


    produto6 = models.CharField('Produto 6', max_length=25, null=True, blank=True)
    categoria6 = models.CharField('Categoria 6', max_length=100, null=True, blank=True)
    valor_base6 = models.CharField('Valor Base 6', max_length=9, null=True, blank=True)
    unidade_medida6 = models.CharField('Unidade de Medida 6', max_length=9, null=True, blank=True)
    quantidade6 = models.CharField('Quantidade 6', max_length=5, null=True, blank=True)
    marca6 = models.CharField('Marca 6', max_length=9, null=True, blank=True)


    produto7 = models.CharField('Produto 7', max_length=25, null=True, blank=True)
    categoria7 = models.CharField('Categoria 7', max_length=100, null=True, blank=True)
    valor_base7 = models.CharField('Valor Base 7', max_length=9, null=True, blank=True)
    unidade_medida7 = models.CharField('Unidade de Medida 7', max_length=9, null=True, blank=True)
    quantidade7 = models.CharField('Quantidade 7', max_length=5, null=True, blank=True)
    marca7 = models.CharField('Marca 7', max_length=9, null=True, blank=True)


    produto8 = models.CharField('Produto 8', max_length=25, null=True, blank=True)
    categoria8 = models.CharField('Categoria 8', max_length=100, null=True, blank=True)
    valor_base8 = models.CharField('Valor Base 8', max_length=9, null=True, blank=True)
    unidade_medida8 = models.CharField('Unidade de Medida 8', max_length=9, null=True, blank=True)
    quantidade8 = models.CharField('Quantidade 8', max_length=5, null=True, blank=True)
    marca8 = models.CharField('Marca 8', max_length=9, null=True, blank=True)


    produto9 = models.CharField('Produto 9', max_length=25, null=True, blank=True)
    categoria9 = models.CharField('Categoria 9', max_length=100, null=True, blank=True)
    valor_base9 = models.CharField('Valor Base 9', max_length=9, null=True, blank=True)
    unidade_medida9 = models.CharField('Unidade de Medida 9', max_length=9, null=True, blank=True)
    quantidade9 = models.CharField('Quantidade 9', max_length=5, null=True, blank=True)
    marca9 = models.CharField('Marca 9', max_length=9, null=True, blank=True)


    produto10 = models.CharField('Produto 10', max_length=25, null=True, blank=True)
    categoria10 = models.CharField('Categoria 10', max_length=100, null=True, blank=True)
    valor_base10 = models.CharField('Valor Base 10', max_length=9, null=True, blank=True)
    unidade_medida10 = models.CharField('Unidade de Medida 10', max_length=9, null=True, blank=True)
    quantidade10 = models.CharField('Quantidade10', max_length=5, null=True, blank=True)
    marca10 = models.CharField('Marca 10', max_length=9, null=True, blank=True)


    produto11 = models.CharField('Produto 11', max_length=25, null=True, blank=True)
    categoria11 = models.CharField('Categoria 11', max_length=100, null=True, blank=True)
    valor_base11 = models.CharField('Valor Base 11', max_length=9, null=True, blank=True)
    unidade_medida11 = models.CharField('Unidade de Medida 11', max_length=9, null=True, blank=True)
    quantidade11 = models.CharField('Quantidade 11', max_length=5, null=True, blank=True)
    marca11 = models.CharField('Marca 11', max_length=9, null=True, blank=True)


    produto12 = models.CharField('Produto 12', max_length=25, null=True, blank=True)
    categoria12 = models.CharField('Categoria 12', max_length=100, null=True, blank=True)
    valor_base12 = models.CharField('Valor Base 12', max_length=9, null=True, blank=True)
    unidade_medida12 = models.CharField('Unidade de Medida 12', max_length=9, null=True, blank=True)
    quantidade12 = models.CharField('Quantidade 12', max_length=5, null=True, blank=True)
    marca12 = models.CharField('Marca 12', max_length=9, null=True, blank=True)


    produto13 = models.CharField('Produto 13', max_length=25, null=True, blank=True)
    categoria13 = models.CharField('Categoria 13', max_length=100, null=True, blank=True)
    valor_base13 = models.CharField('Valor Base 13', max_length=9, null=True, blank=True)
    unidade_medida13 = models.CharField('Unidade de Medida 13', max_length=9, null=True, blank=True)
    quantidade13 = models.CharField('Quantidade 13', max_length=5, null=True, blank=True)
    marca13 = models.CharField('Marca 13', max_length=9, null=True, blank=True)


    produto14 = models.CharField('Produto 14', max_length=25, null=True, blank=True)
    categoria14 = models.CharField('Categoria 14', max_length=100, null=True, blank=True)
    valor_base14 = models.CharField('Valor Base 14', max_length=9, null=True, blank=True)
    unidade_medida14 = models.CharField('Unidade de Medida 14', max_length=9, null=True, blank=True)
    quantidade14 = models.CharField('Quantidade 14', max_length=5, null=True, blank=True)
    marca14 = models.CharField('Marca 14', max_length=9, null=True, blank=True)


    produto15 = models.CharField('Produto 15', max_length=25, null=True, blank=True)
    categoria15 = models.CharField('Categoria 15', max_length=100, null=True, blank=True)
    valor_base15 = models.CharField('Valor Base 15', max_length=9, null=True, blank=True)
    unidade_medida15 = models.CharField('Unidade de Medida 15', max_length=9, null=True, blank=True)
    quantidade15 = models.CharField('Quantidade 15', max_length=5, null=True, blank=True)
    marca15 = models.CharField('Marca 15', max_length=9, null=True, blank=True)


    produto16 = models.CharField('Produto 16', max_length=25, null=True, blank=True)
    categoria16 = models.CharField('Categoria 16', max_length=100, null=True, blank=True)
    valor_base16 = models.CharField('Valor Base 16', max_length=9, null=True, blank=True)
    unidade_medida16 = models.CharField('Unidade de Medida 16', max_length=9, null=True, blank=True)
    quantidade16 = models.CharField('Quantidade 16', max_length=5, null=True, blank=True)
    marca16 = models.CharField('Marca 16', max_length=9, null=True, blank=True)


    produto17 = models.CharField('Produto 17', max_length=25, null=True, blank=True)
    categoria17 = models.CharField('Categoria 17', max_length=100, null=True, blank=True)
    valor_base17 = models.CharField('Valor Base 17', max_length=9, null=True, blank=True)
    unidade_medida17 = models.CharField('Unidade de Medida 17', max_length=9, null=True, blank=True)
    quantidade17 = models.CharField('Quantidade 17', max_length=5, null=True, blank=True)
    marca17 = models.CharField('Marca 17', max_length=9, null=True, blank=True)


    produto18 = models.CharField('Produto 18', max_length=25, null=True, blank=True)
    categoria18 = models.CharField('Categoria 18', max_length=100, null=True, blank=True)
    valor_base18 = models.CharField('Valor Base 18', max_length=9, null=True, blank=True)
    unidade_medida18 = models.CharField('Unidade de Medida 18', max_length=9, null=True, blank=True)
    quantidade18 = models.CharField('Quantidade 18', max_length=5, null=True, blank=True)
    marca18 = models.CharField('Marca 18', max_length=9, null=True, blank=True)


    produto19 = models.CharField('Produto 19', max_length=25, null=True, blank=True)
    categoria19 = models.CharField('Categoria 19', max_length=100, null=True, blank=True)
    valor_base19 = models.CharField('Valor Base 19', max_length=9, null=True, blank=True)
    unidade_medida19 = models.CharField('Unidade de Medida 19', max_length=9, null=True, blank=True)
    quantidade19 = models.CharField('Quantidade 19', max_length=5, null=True, blank=True)
    marca19 = models.CharField('Marca 19', max_length=9, null=True, blank=True)


    produto20 = models.CharField('Produto 20', max_length=25, null=True, blank=True)
    categoria20 = models.CharField('Categoria 20', max_length=100, null=True, blank=True)
    valor_base20 = models.CharField('Valor Base 20', max_length=9, null=True, blank=True)
    unidade_medida20 = models.CharField('Unidade de Medida 20', max_length=9, null=True, blank=True)
    quantidade20 = models.CharField('Quantidade 20', max_length=5, null=True, blank=True)
    marca20 = models.CharField('Marca 20', max_length=9, null=True, blank=True)


    class Meta:
        verbose_name ='Pedido_de_cotacao'
        verbose_name_plural ='Pedidos_de_cotacao'


    def __str__(self):
        return str(self.nome)   

    
class Sala_de_leilao(models.Model):
    pedido = models.CharField('Pedido_de_cotacao', max_length=20)

    class Meta:
        verbose_name ='Sala_de_leilao'
        verbose_name_plural ='Salas_de_leilao'
        

    def __str__(self):
        return str(self.pedido)   