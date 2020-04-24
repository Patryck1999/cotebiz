from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Fornecedor, Categoria, Email_fornecedor, Cliente, Produto, Pedido_de_cotacao
from .forms import FornecedorForm, CategoriaForm, Email_fornecedorForm, Pedido_de_cotacaoForm

def login_user(request):
    return render(request, 'login.html')
    
@csrf_protect
def login_submit(request):
    if request.POST:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuario ou senha inválido. Favor tentar novamente')
    return redirect('/login_user/')
    
@login_required(login_url='/login_user/')
def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login_user/')

@login_required(login_url='/login_user/')
def home(request):
    return render(request, 'index.html')

@login_required(login_url='/login_user/')
def listar_fornecedores(request):
    if str(request.user) == 'admin':
        fornecedores = Fornecedor.objects.all()
        return render(request, 'listar_fornecedores.html', {'fornecedores': fornecedores})
    else:
        return redirect('/')

@login_required(login_url='/login_user/')
def cadastrar_fornecedor(request):
    if str(request.user) == 'admin':
        form = FornecedorForm(request.POST or None)
        context = {
            'form': form
        }
        if (request.method)== 'POST':
            if form.is_valid():
                form.save()
                return redirect('listar_fornecedores')
            else:
                messages.error(request, 'Erro ao cadastrar Fornecedor! Fornecedor já está cadastrado!')
        return render(request, 'cadastrar_fornecedor.html', context)

        

@login_required(login_url='/login_user/')
def fornecedor_detalhar(request, id):
    if str(request.user) == 'admin':
        fornecedor = Fornecedor.objects.get(id=id)
        context = {
            'fornecedor':fornecedor
        }
        return render(request, 'detalhar_fornecedor.html', context)
    else:
        return redirect('/')


@login_required(login_url='/login_user/')
def atualizar_fornecedor(request, id):
    if str(request.user) == 'admin':
        fornecedor = Fornecedor.objects.get(id=id)
        form = FornecedorForm(request.POST or None, instance= fornecedor)
        context = {
            'form': form,
            'fornecedor': fornecedor
        }
        if form.is_valid():
            form.save()
            return redirect('listar_fornecedores')
        return render(request, 'atualizar_fornecedor.html', context)
    else:
        return redirect('/')


@login_required(login_url='/login_user/')
def delete_fornecedor(request, id):
    if str(request.user) == 'admin':
        fornecedor = Fornecedor.objects.get(id=id)
        fornecedor.delete()
        return redirect('listar_fornecedores')
    else:
        return redirect('/')


@login_required(login_url='/login_user/')
def adicionar_pedido(request):
    if str(request.user) == 'admin':
        produtos = Produto.objects.all()
        clientes = Cliente.objects.all()
        emails = Email_fornecedor.objects.all()
        context = {
            'produtos': produtos,
            'clientes': clientes,
            'emails': emails,

        }
        return render(request, 'pedido.html', context)
    else: 
        return redirect('/')

def adicionar_produto(request):
    if str(request.user) == 'admin':
        form = Pedido_de_cotacaoForm(request.POST or None)
        produtos = Produto.objects.all()
        quantidade = Pedido_de_cotacao.objects.all()
        context = {
            produtos:'produtos',
            quantidade:'quantidade',
            form:'form'
        }

        
        return render(request, 'pedido.html', context)
    else: 
        return redirect('/')


@login_required(login_url='/login_user/')
def adicionar_categoria(request):
    if str(request.user) == 'admin':
        form = CategoriaForm(request.POST or None)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('cadastrar_fornecedor')
        return render(request, 'adicionar_categoria.html', context)
    else:
        return redirect('/')

@login_required(login_url='/login_user/')
def adicionar_email_fornecedor(request):
    if str(request.user) == 'admin':
        form = Email_fornecedorForm(request.POST or None)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('cadastrar_fornecedor')
        return render(request, 'adicionar_email_fornecedor.html', context)
    else:
        return redirect('/')

