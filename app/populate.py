from app import db
from app.models import Client

# POPULANDO O BANCO --------------------------------------------------


def reset():
    db.drop_all()
    db.create_all()


def populate():
    # adicionando clientes ---------------------------------------------
    lista_clientes = [
        Client("pedro", "pedro@cliente.com", 'pedro.jpg'),
        Client("jose", "jose@cliente.com", 'jose.jpg'),
        Client("joao", "joao@cliente.com", 'joao.jpg'),
        Client("maria", "maria@cliente.com", 'maria.jpg'),

    ]
    for a in lista_clientes:
        try:
            db.session.add(a)
            print("cliente adicionado!")
            db.session.commit()
        except:
            print("Erro ao adicionar cliente!")
