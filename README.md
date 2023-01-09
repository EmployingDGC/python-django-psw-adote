# python-django-psw-adote

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

## Estrutura de Pastas

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
