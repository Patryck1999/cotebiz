# Projeto_OPE-site-
Site de leilão reverso da cotebiz
ideia do leilão reverso é facilitar a rotina de um intermediador através de uma plataforma, para que ele possa cotar diversos produtos, tendo como base do valor do produto que procura e assim varios fornedores distintos podem lançar seus respectivos valores, sendo o melhor preço o vencedor.

/////////////////////////

No visual Studio faça as seguintes tarefas:

passo 1 - Criar virtualenv

python -m venv nome_dado_a_ser_dado_ao_virtual_env

passo 2 - ativar o virtual env

.\nome_dado_ao_virtual_env\Scripts\activate

passo 3 - Instalar os requisitos para rodar o projeto 

pip install -r requeriments.txt

passo 4 - migrar as tabelas default

python manage.py makemigrations

passo 5 - aplicar as migrações das tabelas default

python manage.py migrate

passo 6- criar usuario para logar como admin

python manage.py createsuperuser

passo 7 - apos estes comandos todos podemos executar nosso programa da seguinte maneira:

python manage.py runserver

passo 8 - clicar no link para acessar

Link: http://127.0.0.1:8000/ ou colar no navegador e caso queira adicionar usuarios acessando http://127.0.0.1:8000/admin será possivel
