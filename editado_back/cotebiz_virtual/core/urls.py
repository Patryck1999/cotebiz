from django.urls import path
from core import views

urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('login_user/submit', views.login_submit, name='login_submit'),
    path('logout/', views.logout_user, name='logout_user'),
    path('', views.home, name='home'),
    path('envio_de_email_fornecedor/', views.envio_de_email_fornecedor, name='envio_de_email_fornecedor'),   
    path('send_email/', views.SendFormEmail.as_view(), name='send_email'),
    path('cadastrar_fornecedor/', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('adicionar_pedido/', views.adicionar_pedido, name='adicionar_pedido'),
    path('adicionar_pedido/submit', views.adicionar_pedido_submit, name='adicionar_pedido/submit'),
    path('adicionar_categoria/', views.adicionar_categoria, name='adicionar_categoria'),
    path('adicionar_email_fornecedor/', views.adicionar_email_fornecedor, name='adicionar_email_fornecedor'),
    path('listar_fornecedores/', views.listar_fornecedores, name='listar_fornecedores'),
    path('listar_produtos_cotados/', views.listar_produtos_cotados, name='listar_produtos_cotados'),
    path('lista_de_pedidos/', views.lista_de_pedidos, name='lista_de_pedidos'),
    path('lista_de_sala_de_leilao/', views.lista_de_sala_de_leilao, name='lista_de_sala_de_leilao'),
    path('detalhar_fornecedor/<id>/', views.detalhar_fornecedor, name='detalhar_fornecedor'),
    path('detalhar_pedido/<id>/', views.detalhar_pedido, name='detalhar_pedido'),
    path('detalhar_produtos_cotados/<id>/', views.detalhar_produtos_cotados, name='detalhar_produtos_cotados'),
    path('detalhar_pedido_da_sala_de_leilao/<id>/', views.detalhar_pedido_da_sala_de_leilao, name='detalhar_pedido_da_sala_de_leilao'),
    path('detalhar_pedido_da_sala_de_leilao/<id>/submit', views.detalhar_pedido_da_sala_de_leilao_submit, name='detalhar_pedido_da_sala_de_leilao_submit'),
    path('atualizar_fornecedor/<int:id>/', views.atualizar_fornecedor, name='atualizar_fornecedor'),
    path('atualizar_pedido/<int:id>/', views.atualizar_pedido, name='atualizar_pedido'),
    path('delete/<int:id>/', views.delete_fornecedor, name='delete_fornecedor'),   
    
]

# CRUD - CREATE, READ, UPDATE, DELETE