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

from app.controllers.feed import feed
app.register_blueprint(feed)

from app.controllers.post import post
app.register_blueprint(post)

from app.controllers.details import post_detail
app.register_blueprint(post_detail)

from app.controllers.user import user
app.register_blueprint(user)