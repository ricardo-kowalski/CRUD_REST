from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
import os


# Inicializando a aplicação
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'banco.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'chave-muito-secreta'

app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'

# Inicializando Banco
db = SQLAlchemy(app)

# Inicializando Marshmallow
# ma = Marshmallow(app)
