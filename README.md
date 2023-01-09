# python-django-psw-adote

---

## Inicialização do projeto

**Criação do ambiente virtual python**

`python -m venv .venv`

**Bibliotecas Utilizadas**

`django` Framework de desenvolvimento
`pillow` Manipulação de Imagens

**Instalar todas as bibliotecas necessárias**

`pip install -r requirements.txt`

**Criação do projeto Django**

`django-admin startproject <nome-projeto> <caminho-onde-sera-criado>`

---

## Criação de `APPs`
Cada `app` é uma parte da aplicação, como se fosse templates. Sempre que for 
criado um novo `app` é necessário registrar no `settings.py` dentro da lista 
`INSTALLED_APPS`

`python manage.py startapp <nome-do-app>`

cada `app` pode ter várias `urls`, para cria-las é necessário criar o arquivo 
`url.py` dentro do seu `app` com o seguinte template

```py
from django.urls import path

from . import views


urlpatterns = [
    path("path-name/", views.function, name="url_name"),
]
```

---

## Estrutura de Pastas

### `manage.py`
É o `cli` da aplicação, utilizado sempre que precisar executar algum comando

`python manage.py <command>`

**Exemplo:**
`python manage.py runserver` Rodar o servidor
`python manage.py migrate` Executar migrações

### `adote/`
É a pasta `core` do projeto, onde ficará as configurações iniciais

### `adote/asgi.py`
`Asynchronous Server Get Interface` utilizado para deploy da aplicação

### `adote/settings.py`
Configurações básicas do projeto

### `adote/urls.py`
Responsável por criar os `endpoints` da aplicação

### `adote/wsgi.py`
`Web Server Get Interface` utilizado para deploy da aplicação

---
