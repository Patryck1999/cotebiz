from django.urls import path
from core import views

urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('login_user/submit', views.login_submit, name='login_submit'),
    path('logout/', views.logout_user, name='logout_user'),
    path('', views.index, name='index'),
    path('enviar_email_fornecedor/', views.enviar_email_fornecedor, name='enviar_email_fornecedor'),   
    path('send_email/', views.SendFormEmail.as_view(), name='send_email'),
    path('cadastrar_fornecedor/', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('criar_pedido/', views.criar_pedido, name='criar_pedido'),
    path('criar_pedido/submit', views.criar_pedido_submit, name='criar_pedido_submit'),
    path('listar_fornecedores/', views.listar_fornecedores, name='listar_fornecedores'),
    path('listar_produtos_cotados/', views.listar_produtos_cotados, name='listar_produtos_cotados'),
    path('listar_pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('listar_salas_de_leilao/', views.listar_salas_de_leilao, name='listar_salas_de_leilao'),
    path('detalhar_fornecedor/<int:id>/', views.detalhar_fornecedor, name='detalhar_fornecedor'),
    path('detalhar_pedido/<int:id>/', views.detalhar_pedido, name='detalhar_pedido'),
    path('detalhar_produtos_cotados/<int:id>/', views.detalhar_produtos_cotados, name='detalhar_produtos_cotados'),
    path('detalhar_pedido_da_sala_de_leilao/<int:id>/', views.detalhar_pedido_da_sala_de_leilao, name='detalhar_pedido_da_sala_de_leilao'),
    path('detalhar_pedido_da_sala_de_leilao/<int:id>/submit', views.detalhar_pedido_da_sala_de_leilao_submit, name='detalhar_pedido_da_sala_de_leilao_submit'),
    path('atualizar_fornecedor/<int:id>/', views.atualizar_fornecedor, name='atualizar_fornecedor'),
    path('deletar_fornecedor/<int:id>/', views.deletar_fornecedor, name='deletar_fornecedor'),   
]
