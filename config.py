import os
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'BIG_SECRET_KEY'


# testes a serem revistos
HOST="0.0.0.0"
PORT= int(os.enviromen.get("PORT",5000))