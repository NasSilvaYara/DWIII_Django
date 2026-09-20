# Gerenciador de Produtos (Django)

Projeto web desenvolvido em Python e Django para gestão de cadastro de produtos.

## Como executar o projeto

1. Ativar o ambiente virtual:
venv\Scripts\activate

2. Instalar as dependências:
pip install django

3. Executar as migrações da base de dados:
python manage.py migrate

4. Iniciar o servidor de desenvolvimento:
python manage.py runserver

## Validações do Formulário
- O preço do produto deve ser estritamente maior que zero.
- A quantidade em estoque não pode ser um número negativo.