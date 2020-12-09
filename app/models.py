from app import db


# Modelos (geram as tabelas do banco de dados usando o ORM SQLAlchemy)

class Client(db.Model):
    __clients__ = 'clients'
    id_client = db.Column(db.Integer, db.Sequence(
        "seq_client"), primary_key=True, nullable=False)
    name_client = db.Column(db.String(100), nullable=False)
    email_client = db.Column(db.String(100), nullable=False)
    photo = db.Column(db.String(250), nullable=True,
                      server_default='person-icon.png')

    def __init__(self, name_client, email_client, photo):
        self.name_client = name_client
        self.email_client = email_client
        self.photo = photo


class Product(db.Model):
    __product__ = 'product'
    id_prod = db.Column(db.Integer, db.Sequence(
        "seq_prod"), primary_key=True, nullable=False)
    name_prod = db.Column(db.String(50), nullable=False)
    initial_date = db.Column(db.Date, nullable=False)
    final_date = db.Column(db.Date, nullable=True)
    desc_prod = db.Column(db.String(500), nullable=True)

    def __init__(self, name_prod, initial_date, final_date, desc_prod):
        self.name_prod = name_prod
        self.initial_date = initial_date
        self.final_date = final_date
        self.desc_prod = desc_prod
