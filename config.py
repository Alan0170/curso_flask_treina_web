DEBUG = True # Inserida apenas no setor de desenvolvimento para testes

USERNAME = 'root'
PASSWORD = 'A1l2a1l22.0'
SERVER = 'localhost'
DB = 'flask_fundamentos'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
