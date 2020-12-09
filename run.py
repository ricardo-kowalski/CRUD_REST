from flask import jsonify, request
from app import app
from app.populate import populate, reset
from app.models import Client
from app import db

# INICIANDO BANCO (cria um comando do tipo flask
# <comando> utilizdo para criar e popular o banco)


@app.cli.command("initdb")
def reset_db():
    reset()

    print("Banco Resetado!")


@app.cli.command("populatedb")
def populate_db():
    reset()
    populate()

    print("Banco Populado!")


# @app.route('/', methods=['GET'])
# def home():
#     return jsonify({'msg': 'API REST'})


@app.route('/client/all', methods=['GET'])
def get_clients():
    '''Retorna lista com nome, email e url da foto de todos os clientes'''

    all_clients = Client.query.all()

    return jsonify(clients=[i.serialize for i in all_clients])


@app.route('/client/id/<int:id_cli>', methods=['GET'])
def get_client_by_id(id_cli):
    '''Retorna lista com nome, email e url da foto do cliente solicitado'''

    client = Client.query.filter_by(id_client=id_cli).first()

    return jsonify(client=[client.serialize])


@app.route('/client/name/<name_cli>', methods=['GET'])
def get_client_by_name(name_cli):
    '''Retorna lista com nome, email e url da foto do cliente solicitado'''

    client = Client.query.filter_by(name_client=name_cli.lower()).first()

    return jsonify(client=[client.serialize])


@app.route('/client', methods=['POST'])
def save_client():
    '''Adiciona cliente ao banco'''
    name = request.json['name']
    email = request.json['email']
    photo = request.json['photo']

    new_client = Client(name, email, photo)

    db.session.add(new_client)
    db.session.commit()

    return jsonify(new_client.serialize)


@app.route('/client/<int:id_cli>', methods=['PUT'])
def update_client(id_cli):
    '''Modifica um cliente no banco'''

    client = Client.query.get(id_cli)

    updt_name = request.json['name']
    updt_email = request.json['email']
    updt_photo = request.json['photo']

    client.name_client = updt_name
    client.email_client = updt_email
    client.photo = updt_photo

    db.session.commit()

    return jsonify(client.serialize)


@app.route('/client/<int:id_cli>', methods=['DELETE'])
def delete_client(id_cli):
    """Deleta um cliente por id"""
    client = Client.query.get(id_cli)
    db.session.delete(client)
    db.session.commit()

    return jsonify(client.serialize)


# Rodando o servidor
if __name__ == '__main__':
    app.run(debug=True)
