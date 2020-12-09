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

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id_client,
            'name': self.name_client,
            'email': self.email_client,
            'photo': self.photo
        }
