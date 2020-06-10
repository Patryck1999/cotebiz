from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.views.generic import View
from django.core.mail import send_mail

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
def envio_de_email_fornecedor(request):
    pedido = Pedido_de_cotacao.objects.all()
    context={
        'pedido':pedido
    }
    return render(request, 'email_fornecedor.html', context)

class SendFormEmail(View):

    def get(self, request):

        # Get the form data 
        email = request.GET.get('email', None)
        name="Olá nós da COTEBIZ, temos uma nova cotação para você parceiro entre em nossa plataforma!"
        emails=[]
        message = request.GET.get('mensagem', None)
        for e in email.split(','):
            emails.append(e.strip())
        print(emails)
        # Send Email
        send_mail(
            'Nova cotação disponivel - Cotebiz', 
            name + "\n" + message, 
            'sender@example.com', # Admin
                emails,
        ) 

        # Redirect to same page after form submit
        return redirect('home') 

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
def adicionar_pedido(request):
    if str(request.user) == 'admin':
        return render(request, 'criar_pedido.html')
    else:
        return redirect('/')
        
@login_required(login_url='/login_user/')
def adicionar_pedido_submit(request):
    numero_do_pedido = request.POST.get('numero_do_pedido')
    data = request.POST.get('data')
    nome = request.POST.get('nome')
    razao_social = request.POST.get('razao_social')
    cnpj = request.POST.get('cnpj')
    plano = request.POST.get('plano')
    cep = request.POST.get('cep')
    rua = request.POST.get('rua')
    bairro = request.POST.get('bairro')
    cidade = request.POST.get('cidade')
    numero = request.POST.get('numero')
    telefone = request.POST.get('telefone')
    celular = request.POST.get('celular')
    email = request.POST.get('email')
     
    produto1 = request.POST.get('produto1')
    categoria1 = request.POST.get('categoria1')
    valor_base1= request.POST.get('valor_base1')
    unidade_medida1 = request.POST.get('unidade_medida1')
    quantidade1 = request.POST.get('quantidade1')
    marca1 = request.POST.get('marca1')

    produto2 = request.POST.get('produto2')
    categoria2 = request.POST.get('categoria2')
    valor_base2= request.POST.get('valor_base2')
    unidade_medida2 = request.POST.get('unidade_medida2')
    quantidade2 = request.POST.get('quantidade2')
    marca2 = request.POST.get('marca2')

    produto3 = request.POST.get('produto3')
    categoria3 = request.POST.get('categoria3')
    valor_base3= request.POST.get('valor_base3')
    unidade_medida3 = request.POST.get('unidade_medida3')
    quantidade3 = request.POST.get('quantidade3')
    marca3 = request.POST.get('marca3')

    produto4 = request.POST.get('produto4')
    categoria4 = request.POST.get('categoria4')
    valor_base4= request.POST.get('valor_base4')
    unidade_medida4 = request.POST.get('unidade_medida4')
    quantidade4 = request.POST.get('quantidade4')
    marca4 = request.POST.get('marca4')

    produto5 = request.POST.get('produto5')
    categoria5 = request.POST.get('categoria5')
    valor_base5= request.POST.get('valor_base5')
    unidade_medida5 = request.POST.get('unidade_medida5')
    quantidade5 = request.POST.get('quantidade5')
    marca5 = request.POST.get('marca5')

    produto6 = request.POST.get('produto6')
    categoria6 = request.POST.get('categoria6')
    valor_base6= request.POST.get('valor_base6')
    unidade_medida6 = request.POST.get('unidade_medida6')
    quantidade6 = request.POST.get('quantidade6')
    marca6 = request.POST.get('marca6')

    produto7 = request.POST.get('produto7')
    categoria7 = request.POST.get('categoria7')
    valor_base7= request.POST.get('valor_base7')
    unidade_medida7 = request.POST.get('unidade_medida7')
    quantidade7 = request.POST.get('quantidade7')
    marca7 = request.POST.get('marca7')

    produto8 = request.POST.get('produto8')
    categoria8 = request.POST.get('categoria8')
    valor_base8= request.POST.get('valor_base8')
    unidade_medida8 = request.POST.get('unidade_medida8')
    quantidade8 = request.POST.get('quantidade8')
    marca8 = request.POST.get('marca8')

    produto9 = request.POST.get('produto9')
    categoria9 = request.POST.get('categoria9')
    valor_base9= request.POST.get('valor_base9')
    unidade_medida9 = request.POST.get('unidade_medida9')
    quantidade9 = request.POST.get('quantidade9')
    marca9 = request.POST.get('marca9')

    produto10 = request.POST.get('produto10')
    categoria10 = request.POST.get('categoria10')
    valor_base10= request.POST.get('valor_base10')
    unidade_medida10 = request.POST.get('unidade_medida10')
    quantidade10 = request.POST.get('quantidade10')
    marca10 = request.POST.get('marca10')

    produto11 = request.POST.get('produto11')
    categoria11 = request.POST.get('categoria11')
    valor_base11= request.POST.get('valor_base11')
    unidade_medida11 = request.POST.get('unidade_medida11')
    quantidade11 = request.POST.get('quantidade11')
    marca11 = request.POST.get('marca11')

    produto12 = request.POST.get('produto12')
    categoria12 = request.POST.get('categoria12')
    valor_base12= request.POST.get('valor_base12')
    unidade_medida12 = request.POST.get('unidade_medida12')
    quantidade12 = request.POST.get('quantidade12')
    marca12 = request.POST.get('marca12')

    produto13 = request.POST.get('produto13')
    categoria13 = request.POST.get('categoria13')
    valor_base13= request.POST.get('valor_base13')
    unidade_medida13 = request.POST.get('unidade_medida13')
    quantidade13 = request.POST.get('quantidade13')
    marca13 = request.POST.get('marca13')

    produto14 = request.POST.get('produto14')
    categoria14 = request.POST.get('categoria14')
    valor_base14= request.POST.get('valor_base14')
    unidade_medida14 = request.POST.get('unidade_medida14')
    quantidade14 = request.POST.get('quantidade14')
    marca14 = request.POST.get('marca14')

    produto15 = request.POST.get('produto15')
    categoria15 = request.POST.get('categoria15')
    valor_base15= request.POST.get('valor_base15')
    unidade_medida15 = request.POST.get('unidade_medida15')
    quantidade15 = request.POST.get('quantidade15')
    marca15 = request.POST.get('marca15')

    produto16 = request.POST.get('produto16')
    categoria16 = request.POST.get('categoria16')
    valor_base16= request.POST.get('valor_base16')
    unidade_medida16 = request.POST.get('unidade_medida16')
    quantidade16 = request.POST.get('quantidade16')
    marca16 = request.POST.get('marca16')

    produto17 = request.POST.get('produto17')
    categoria17 = request.POST.get('categoria17')
    valor_base17= request.POST.get('valor_base17')
    unidade_medida17 = request.POST.get('unidade_medida17')
    quantidade17 = request.POST.get('quantidade17')
    marca17 = request.POST.get('marca17')

    produto18 = request.POST.get('produto18')
    categoria18 = request.POST.get('categoria18')
    valor_base18= request.POST.get('valor_base18')
    unidade_medida18 = request.POST.get('unidade_medida18')
    quantidade18 = request.POST.get('quantidade18')
    marca18 = request.POST.get('marca18')

    produto19 = request.POST.get('produto19')
    categoria19 = request.POST.get('categoria19')
    valor_base19= request.POST.get('valor_base19')
    unidade_medida19 = request.POST.get('unidade_medida19')
    quantidade19 = request.POST.get('quantidade19')
    marca19 = request.POST.get('marca19')

    produto20 = request.POST.get('produto20')
    categoria20 = request.POST.get('categoria20')
    valor_base20= request.POST.get('valor_base20')
    unidade_medida20 = request.POST.get('unidade_medida20')
    quantidade20 = request.POST.get('quantidade20')
    marca20 = request.POST.get('marca20')

    pedido = Pedido_de_cotacao.objects.create(n_pedido=numero_do_pedido, data_agora=data, nome=nome, razao_social=razao_social,
            cnpj=cnpj, plano=plano, cep=cep,rua=rua, bairro=bairro, cidade=cidade,
            numero=numero, telefone=telefone, celular=celular, email=email,
            produto1=produto1, categoria1=categoria1, valor_base1=valor_base1, unidade_medida1=unidade_medida1, marca1=marca1, quantidade1=quantidade1,
            produto2=produto2, categoria2=categoria2, valor_base2=valor_base2, unidade_medida2=unidade_medida2, marca2=marca2, quantidade2=quantidade2,
            produto3=produto3, categoria3=categoria3, valor_base3=valor_base3, unidade_medida3=unidade_medida3, marca3=marca3, quantidade3=quantidade3,
            produto4=produto4, categoria4=categoria4, valor_base4=valor_base4, unidade_medida4=unidade_medida4, marca4=marca4, quantidade4=quantidade4,
            produto5=produto5, categoria5=categoria5, valor_base5=valor_base5, unidade_medida5=unidade_medida5, marca5=marca5, quantidade5=quantidade5,
            produto6=produto6, categoria6=categoria6, valor_base6=valor_base6, unidade_medida6=unidade_medida6, marca6=marca6, quantidade6=quantidade6,
            produto7=produto7, categoria7=categoria7, valor_base7=valor_base7, unidade_medida7=unidade_medida7, marca7=marca7, quantidade7=quantidade7,
            produto8=produto8, categoria8=categoria8, valor_base8=valor_base8, unidade_medida8=unidade_medida8, marca8=marca8, quantidade8=quantidade8,
            produto9=produto9, categoria9=categoria9, valor_base9=valor_base9, unidade_medida9=unidade_medida9, marca9=marca9, quantidade9=quantidade9,
            produto10=produto10, categoria10=categoria10, valor_base10=valor_base10, unidade_medida10=unidade_medida10, marca10=marca10, quantidade10=quantidade10,
            produto11=produto11, categoria11=categoria11, valor_base11=valor_base11, unidade_medida11=unidade_medida11, marca11=marca11, quantidade11=quantidade11,
            produto12=produto12, categoria12=categoria12, valor_base12=valor_base12, unidade_medida12=unidade_medida12, marca12=marca12, quantidade12=quantidade12,
            produto13=produto13, categoria13=categoria13, valor_base13=valor_base13, unidade_medida13=unidade_medida13, marca13=marca13, quantidade13=quantidade13,
            produto14=produto14, categoria14=categoria14, valor_base14=valor_base14, unidade_medida14=unidade_medida14, marca14=marca14, quantidade14=quantidade14,
            produto15=produto15, categoria15=categoria15, valor_base15=valor_base15, unidade_medida15=unidade_medida15, marca15=marca15, quantidade15=quantidade15,
            produto16=produto16, categoria16=categoria16, valor_base16=valor_base16, unidade_medida16=unidade_medida16, marca16=marca16, quantidade16=quantidade16,
            produto17=produto17, categoria17=categoria17, valor_base17=valor_base17, unidade_medida17=unidade_medida17, marca17=marca17, quantidade17=quantidade17,
            produto18=produto18, categoria18=categoria18, valor_base18=valor_base18, unidade_medida18=unidade_medida18, marca18=marca18, quantidade18=quantidade18,
            produto19=produto19, categoria19=categoria19, valor_base19=valor_base19, unidade_medida19=unidade_medida19, marca19=marca19, quantidade19=quantidade19,
            produto20=produto20, categoria20=categoria20, valor_base20=valor_base20, unidade_medida20=unidade_medida20, marca20=marca20, quantidade20=quantidade20
            )

    return redirect('envio_de_email_fornecedor')

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

@login_required(login_url='/login_user/')
def listar_fornecedores(request):
    if str(request.user) == 'admin':
        fornecedores_all = Fornecedor.objects.all()
        fornecedor_query = request.GET.get('fornecedor')
        cnpj_query = request.GET.get('cnpj')
        categoria_query = request.GET.get('categoria')

        if fornecedor_query != '' and fornecedor_query is not None:
            fornecedores_all = fornecedores_all.filter(fornecedor__icontains=fornecedor_query)

        if cnpj_query != '' and cnpj_query is not None:
            fornecedores_all = fornecedores_all.filter(cnpj__icontains=cnpj_query)

        if categoria_query != '' and categoria_query is not None:
            fornecedores_all = fornecedores_all.filter(categoria__icontains=categoria_query)

        context={
            'fornecedores_all': fornecedores_all
        }

        return render(request, "listar_fornecedores.html", context) 
    else:
        return redirect('/')

@login_required(login_url='/login_user/')
def listar_produtos_cotados(request):
    if str(request.user) == 'admin':
        produtos_cotados = Pedido_de_cotacao_fornecedor.objects.all()
        context = {
            'produtos_cotados':produtos_cotados
        }
        return render(request, 'listar_produtos_cotados.html', context)
    else:
        return redirect('/')

def lista_de_pedidos(request):
    if str(request.user) == 'admin':
        pedido = Pedido_de_cotacao.objects.all()
        n_pedido_query = request.GET.get('numero_pedido')
        razao_social_query = request.GET.get('razao_social')
        cnpj_query = request.GET.get('id_cnpj')
            
        if n_pedido_query != '' and n_pedido_query is not None:
            pedido = pedido.filter(n_pedido__icontains=n_pedido_query)

        if razao_social_query != '' and razao_social_query is not None:
            pedido = pedido.filter(razao_social__icontains=razao_social_query)

        if cnpj_query != '' and cnpj_query is not None:
            pedido = pedido.filter(cnpj__icontains=cnpj_query)

        context={
            'pedido': pedido
        }

        return render(request, "lista_de_pedidos.html", context)
    else:
        return redirect('/')

@login_required(login_url='/login_user/')
def lista_de_sala_de_leilao(request):
    if str(request.user) == 'admin':
        pedido = Pedido_de_cotacao.objects.all()
        n_pedido_query = request.GET.get('n_pedido')
        nome_query = request.GET.get('nome')
            
        if n_pedido_query != '' and n_pedido_query is not None:
            pedido = pedido.filter(id=n_pedido_query)

        if nome_query != '' and nome_query is not None:
            pedido = pedido.filter(nome__icontains=nome_query)


        context={
            'pedido': pedido
        }

        return render(request, "lista_de_sala_de_leilao.html", context)
    else:
        return redirect('/')

@login_required(login_url='/login_user/')
def detalhar_fornecedor(request, id):
    if str(request.user) == 'admin':
        fornecedor = Fornecedor.objects.get(id=id)
        context = {
            'fornecedor':fornecedor
        }
        return render(request, 'detalhar_fornecedor.html', context)
    else:
        return redirect('/')

def detalhar_pedido(request, id):
    if str(request.user) == 'admin':
        pedido = Pedido_de_cotacao.objects.get(id=id)
        context = {
            'pedido':pedido
        }
        return render(request, 'detalhar_pedidos.html', context)
    else:
        return redirect('/')

@login_required(login_url='/login_user/')
def detalhar_pedido_da_sala_de_leilao(request, id):
    if str(request.user) == 'admin':
        pedido = Pedido_de_cotacao.objects.get(id=id)
        context = {
            'pedido':pedido
        }
        return render(request, 'detalhar_pedido_da_sala_de_leilao.html', context)
    else:
        return redirect('/')

@login_required(login_url='/login_user/')
def detalhar_pedido_da_sala_de_leilao_submit(request, id):
    fornecedor = request.POST.get('fornecedor')
    observacao1 = request.POST.get('observacao_1')
    observacao2 = request.POST.get('observacao_2')
    observacao3 = request.POST.get('observacao_3')
    observacao4 = request.POST.get('observacao_4')
    observacao5 = request.POST.get('observacao_5')
    observacao6 = request.POST.get('observacao_6')
    observacao7 = request.POST.get('observacao_7')
    observacao8 = request.POST.get('observacao_8')
    observacao9 = request.POST.get('observacao_9')
    observacao10 = request.POST.get('observacao_10')
    observacao11 = request.POST.get('observacao_11')
    observacao12 = request.POST.get('observacao_12')
    observacao13 = request.POST.get('observacao_13')
    observacao14 = request.POST.get('observacao_14')
    observacao15 = request.POST.get('observacao_15')
    observacao16 = request.POST.get('observacao_16')
    observacao17 = request.POST.get('observacao_17')
    observacao18 = request.POST.get('observacao_18')
    observacao19 = request.POST.get('observacao_19')
    observacao20 = request.POST.get('observacao_20')
    pedido_de_cotacao_fornecedor = Pedido_de_cotacao_fornecedor.objects.create(fornecedor=fornecedor ,observacao_1=observacao1, 
    observacao_2=observacao2, observacao_3=observacao3, observacao_4=observacao4, observacao_5=observacao5,
    observacao_6=observacao6, observacao_7=observacao7, observacao_8=observacao8, observacao_9=observacao9,
    observacao_10=observacao10, observacao_11=observacao11, observacao_12=observacao12, observacao_13=observacao13,
    observacao_14=observacao14, observacao_15=observacao15, observacao_16=observacao16, observacao_17=observacao17,
    observacao_18=observacao18, observacao_19=observacao19, observacao_20=observacao20)
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
        if (request.method)== 'POST':
            if form.is_valid():
                form.save()
                return redirect('listar_fornecedores')
            else:
                messages.error(request, 'Erro ao Atualizar Fornecedor! Fornecedor já está cadastrado!')
        return render(request, 'atualizar_fornecedor.html', context)

@login_required(login_url='/login_user/')        
def atualizar_pedido(request, id):
    if str(request.user) == 'admin':
        fornecedor = Fornecedor.objects.get(id=id)
        context = {
            'form': form,
            'fornecedor': fornecedor
        }
        if (request.method)== 'POST':
            if form.is_valid():
                form.save()
                return redirect('listar_fornecedores')
            else:
                messages.error(request, 'Erro ao Atualizar Fornecedor! Fornecedor já está cadastrado!')
        return render(request, 'atualizar_fornecedor.html', context)   

@login_required(login_url='/login_user/')
def delete_fornecedor(request, id):
    if str(request.user) == 'admin':
        fornecedor = Fornecedor.objects.get(id=id)
        fornecedor.delete()
        return redirect('listar_fornecedores')
    else:
        return redirect('/')
