from flask import Flask
from .views import cliente_view
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

cliente_view.Cliente(app)

from .models import cliente_model

