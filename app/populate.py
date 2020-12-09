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

    # # adicionando produtos -------------------------------------------
    # lista_produtos = [
    #     Product('Leite Italac', datetime.date(2020, 12, 10),
    #             datetime.date(2020, 12, 30), 'Leite integral de caixinha'),
    #     Product('Frango', datetime.date(2020, 12, 1), datetime.date(
    #         2021, 12, 30), 'Peito de frango caipira'),
    #     Product('Cebola', datetime.date(2020, 10, 5), datetime.date(
    #         2021, 8, 10), 'Cebolinha plantada aqui no sítio'),
    #     Product('Bolacha', datetime.date(2020, 9, 10), datetime.date(
    #         2022, 9, 15), 'Bolacha recheada, até pq biscoito é outra coisa'),
    # ]
    # for prod in lista_produtos:
    #     try:
    #         db.session.add(prod)
    #         print("produto adicionado!")
    #         db.session.commit()
    #     except:
    #         print("Erro ao adicionar produto!")
