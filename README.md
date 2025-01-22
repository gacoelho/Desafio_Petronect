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

**manage.py** = arquivo que iniciar o servidor localmente (falarei sobre ele mais abaixo)

**requirements.txt** = todas as dependencias do python para rodar a aplication localmente atraves do comando ```pip install -r requiremts.txt```

**static** = diretório com os arquivos estáticos com style.css

**templates** = diretório com os arquivos HTML de cada página da aplicação.

**to_do**= diretório com toda a funcionalidade da função

**to_do_petronect**= diretório com os arquivos de configuração tanto do backend, quanto urls paths, wsgi e asgi.
