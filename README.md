# Handler Archive CNAB

***O projeto é a implementação de um aplicativo web que recebe, via upload, e processa arquivos CNAB, guarda as informações em banco de dados e disponibiliza a relação das transações cadastradas e o saldo total por beneficiário.***


## Documentação CNAB

- **A tabela abaixo documenta a posição e comprimento das informações no layout utilizado:**

![Documentação da posição e comprimento das informações](https://conteudo-kenzie-fullstack.vercel.app/modulo_6/desafio_backend/img/documentacao_cnab.png)

- **Já a tabela abaixo explana cada um dos tipos de transação:**

![Documentação dos tipos de transação](https://conteudo-kenzie-fullstack.vercel.app/modulo_6/desafio_backend/img/tipo_transacao.png)

## Tecnologias Utilizadas

- **Python**
- **Framework Flask**
- **Flask-SQLAchemy**
- **PostgreSQL**
- **HTML/CSS**
- **Flask-migration**
- **Gunicorn**
- **Docker**


# Rodando a aplicação

Copie o arquivo  `.env.example` para o `.env` e forneça as credenciais do banco de dados que deseja usar

1. Rode os containers com o docker compose:
	```
	docker compose up
	```
	ou

	```
	docker-compose up
	```

**A aplicação estará rodando na porta 8080**

## Rodando em ambiente de produção

1. Primeiro, crie o arquivo `.env` (obs: você pode copiar o arquivo do `.env.example`). Declare sua string de conexão com o banco de dados. O projeto usa **Flask-SQLALchemy** como ORM, confira os dialetos permitidos na [documentação](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)

2.  Crie o ambiente virtal:

	```
	python -m venv venv
	```
3. Ative seu venv:

	 *No Linux:*
	```
	source venv/bin/activate
	```
	*No windows:*
	```
	.\venv\Scripts\activate
	```
4. Instale as dependências do projeto: 
	```
	pip install -r requirements.txt
	```
	****Obs**: Caso esteja utilizando outro dialeto de banco de dados, instale o driver de conexão do banco utilizado.* *

5. Declare a constante  `FLASK_DEBUG=True`

6. Rode o projeto:
	```
	flask run
	```
7. Extra: O projeto também está pronto para rodar no servidor de aplicação WSGI Gunicorn:
	```
	gunicorn "app:app.create_app()"
	```
