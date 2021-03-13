from flask import Blueprint

follows = Blueprint("follows",__name__)

from . import routes