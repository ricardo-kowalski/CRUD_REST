from flask import jsonify
from app import app
from app.populate import populate, reset
from app.models import Client, Product


# INICIANDO BANCO -----------------------------------------------------

@app.cli.command("initdb")
def reset_db():
    reset()

    print("Banco Resetado!")


@app.cli.command("populatedb")
def populate_db():
    reset()
    populate()

    print("Banco Populado!")


@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Ola'})


# Rodando o servidor
if __name__ == '__main__':
    app.run(debug=True)
