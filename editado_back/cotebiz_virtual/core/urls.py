from django.urls import path
from core import views
from core.views import leilao


urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('login_user/submit', views.login_submit, name='login_submit'),
    path('logout/', views.logout_user, name='logout_user'),
    path('', views.home, name='home'),
    path('listar_fornecedores/', views.listar_fornecedores, name='listar_fornecedores'),
    path('cadastrar_fornecedor/', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('fornecedor_detalhar/<id>/', views.fornecedor_detalhar, name='fornecedor_detalhar'),
    path('atualizar_fornecedor/<int:id>/', views.atualizar_fornecedor, name='atualizar_fornecedor'),
    path('delete/<int:id>/', views.delete_fornecedor, name='delete_fornecedor'),
    path('adicionar_pedido/', views.adicionar_pedido, name='adicionar_pedido'),
    path('adicionar_pedido/submit', views.adicionar_pedido_submit, name='adicionar_pedido/submit'),
    path('adicionar_categoria/', views.adicionar_categoria, name='adicionar_categoria'),
    path('adicionar_email_fornecedor/', views.adicionar_email_fornecedor, name='adicionar_email_fornecedor'),   
    path('envio_de_email_fornecedor/', views.envio_de_email_fornecedor, name='envio_de_email_fornecedor'),   
    path('leilao', leilao, name='leilao'),
]



# CRUD - CREATE, READ, UPDATE, DELETE