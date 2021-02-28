from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

ma = Marshmallow(app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.controllers.auth import auth
app.register_blueprint(auth)
