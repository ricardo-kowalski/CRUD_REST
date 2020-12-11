# CRUD_REST
Atividade da matéria de Aplicações Distribuídas (ADID6)

## Instalação 

Prerequisitos:
- Python3
- Pip3
- Virtualenv

Passos:
#1 - clonar repositório
~ git clone https://github.com/ricardo-kowalski/CRUD_REST

#2 - ativar ambiente virtual
~ cd CRUD_REST
~ . venv/bin/activate

#3 - instalar bibliotecas 
~ pip3 install -r requirements.txt

#4 - criando Banco
~ flask initdb
~ flask populatedb

#5 - configurando arquivo de inicialização e tipo de ambiente
export FLASK_ENV=development
export FLASK_APP=app

#6 - rodando o servidor
~ flask run


## API REST (aqui foi utilizado a ferramenta 'curl', mas também podem ser utilizadas Postman ou equivalentes)##

Método: 

GET
curl --request GET '127.0.0.1:5000/'

### Retorna lista com nome, email e url da foto de todos os clientes
~ curl -X GET http://127.0.0.1:5000/client/all

´´´
 saída esperada: 
{
  "json_list": [
    {
      "email": "pedro@cliente.com", 
      "name": "Pedro", 
      "photo": "pedro.jpg"
    }, 
    {
      "email": "jose@cliente.com", 
      "name": "Jose", 
      "photo": "jose.jpg"
    }, 
    {
      "email": "joao@cliente.com", 
      "name": "Joao", 
      "photo": "joao.jpg"
    }, 
    {
      "email": "maria@cliente.com", 
      "name": "Maria", 
      "photo": "maria.jpg"
    }
  ]
} 
´´´

### Retorna lista com nome, email e url da foto de um cliente em específico (por id)
~ curl -X GET http://127.0.0.1:5000/client/id/4

saída esperada:
{
  "client": [
    {
      "email": "maria@cliente.com", 
      "id": 4, 
      "name": "maria", 
      "photo": "maria.jpg"
    }
  ]
}




### Retorna lista com nome, email e url da foto de um cliente em específico (por nome)
~ curl -X GET http://127.0.0.1:5000/client/name/jose

saída esperada:
{
  "client": [
    {
      "email": "jose@cliente.com", 
      "id": 2, 
      "name": "jose", 
      "photo": "jose.jpg"
    }
  ]
}



### Inclui um cliente ao banco
~ curl -H "Content-Type: application/json" -X POST -d '{"name":"carlos","email":"carlos@cliente.com", "photo":"carlos.jpg"}' http://localhost:5000/client

saída esperada:
{
  "email": "gege@cliente.com", 
  "id": 5, 
  "name": "getulio", 
  "photo": "gege.jpg"
}


### Altera um cliente no banco
~ curl -H "Content-Type: application/json" -X PUT -d '{"name":"ferreira","email":"ferreira@cliente.com", "photo":"ferreira.jpg"}' http://localhost:5000/client/2

saída esperada:
  {
  "email": "ferreira@cliente.com", 
  "id": 2, 
  "name": "ferreira", 
  "photo": "ferreira.jpg"
}



### Deleta um cliente do banco
~ curl -X DELETE http://127.0.0.1:5000/client/1

saída esperada:
{
  "email": "pedro@cliente.com", 
  "id": 1, 
  "name": "pedro", 
  "photo": "pedro.jpg"
}

