from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

ma = Marshmallow(app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver',Server(host="0.0.0.0",port=5000,use_debugger=None))

cors = CORS(app, resource={r"/*":{"origins":"*"}})

from app.controllers.auth import auth
app.register_blueprint(auth)

from app.controllers.feed import feed
app.register_blueprint(feed)

from app.controllers.post import posts
app.register_blueprint(posts)

from app.controllers.details import post_detail
app.register_blueprint(post_detail)

from app.controllers.user import user
app.register_blueprint(user)

from app.controllers import controller
app.register_blueprint(controller)

from app.controllers.follow import follows
app.register_blueprint(follows)