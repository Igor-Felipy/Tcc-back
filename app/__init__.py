from flask import Flask

app = Flask(__name__)

from app.controllers import controllers
app.register_blueprint(controllers)