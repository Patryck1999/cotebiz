# Projeto_OPE-site-
Site de leilão reverso da cotebiz

/////////////////////////

No visual Studio faça as seguintes tarefas:

passo 1 - Criar virtualenv

python -m venv nome_dado_a_ser_dado_ao_virtual_env

passo 2 - ativar o virtual env

.\nome_dado_a_ser_dado_ao_virtual_env\Scripts\activate

passo 3 - Instalar o pacote django

python -m pip install django

passo 4 - Fora do Visual Studio Instale o postgres e defina o usuario e senha as mesmas que estão no projeto que sa~os seguintes:

usuario: postgres e senha: g@mer1999p

passo 5 - instale o postbird e configure

Entre com usuario e senha do postgress e crie um banco de dados chamado cotebiz

passo 6 - voltando no visual studio e continuando no ambiente virtual instalar o psycopg2 para integrar com banco de dados postgres

python - m pip install psycopg2

passo 7 - migrar as tabelas default

python manage.py migrate

passo 8- criar usuario para logar como admin

python manage.py createsuperuser

passo 9 - apos estes comandos todos podemos executar nosso programa da seguinte maneira:

python manage.py runserver

passo 10 - clicar no link para acessar

Link: http://127.0.0.1:8000/ ou colar no navegador e caso queira adicionar usuarios acessando http://127.0.0.1:8000/admin será possivel
