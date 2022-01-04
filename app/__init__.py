from flask import Flask
from .views import cliente_view
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

cliente_view.Cliente(app)

