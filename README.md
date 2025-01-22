O APP Web foi desenvolvido usando python usando o framework **Django** para administrar o backend.

O Django administra e modela o banco de dados, no caso dessa aplicaçao usamo o **sqlite** que vem como padrão no django e facilita rodar localmente.
Para uma aplicação mais robusta o PostreSQL devidamente configurado séria melhor.

A estrutura:
```
└── to_do_petronect
    ├── db.sqlite3
    ├── manage.py
    ├── requirements.txt
    ├── static
    ├── templates
    ├── to_do
    └── to_do_petronect
```

**db.sqlite3** = Banco de dados armazenado localmente.

**manage.py** = arquivo que iniciar o servidor localmente

**requirements.txt** = todas as dependencias do python para rodar a aplication localmente atraves do comando 

**static** = diretório com os arquivos estáticos com style.css

**templates** = diretório com os arquivos HTML de cada página da aplicação.

**to_do**= diretório com toda a funcionalidade da função

**to_do_petronect**= diretório com os arquivos de configuração tanto do backend, quanto urls paths, wsgi e asgi.

to_do:

estrutura
```
├── admin.py
├── apps.py
├── forms.py
├── __init__.py
├── migrations
├── models.py
├── __pycache__
├── tests.py
└── views.py
```

**forms.py** = define o form para que o django consigo criar todos os campos necessários pro *modelo Task* quando for requisitado.

**models.py** == define o *modelo Task* com os campos necessários {title (titulo), description (descrição), pub_date(data de criação), due_date(data de entrega da tarefa)}

**views.py** == criar as paginas e renderiza a inteface do frontend. Chamando os HTML corresponde e verificando HTTP methods da requisição ('GET' e 'POST') e retornando ao usário as tarefas.


Aplicação está Rondado no site no https://gacoelho.pythonanywhere.com/

Para rodar localmente no terminal linux, segue os passos:

obs: É necessário já ter o *python* e *git* instalado.

1- Baixar o reposiório:

```git clone https://github.com/gacoelho/Desafio_Petronect.git```

2- Entrar no repositório:

```cd Desafio_Petrocnect```

```cd to_do_petrocnect```

3- Baixar as dependencias:

```pip install -r requirements.txt```

4- Iniciar o servidor local do Django:

```python manage.py makemigrations```

```python manage.py migrate```

```python manage.py runserver```

o site será hospedado localmente no http://127.0.0.1:8000/



