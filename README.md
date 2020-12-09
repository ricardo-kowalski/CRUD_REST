# CRUD_REST
Atividade da matéria de Aplicações Distribuídas (ADID6)

##Instalação##

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
~ flask shell
>> from app import db
>> db.create_all()
>> exit()

export FLASK_ENV=development
export FLASK_APP=app

#5 - rodando o servidor
~ flask run


##Uso##

Método GET
curl --request GET '127.0.0.1:5000/'

