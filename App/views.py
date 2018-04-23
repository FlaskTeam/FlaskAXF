from flask import Blueprint

blue = Blueprint("blue",__name__)
def init_blue(app):
    app.register_blueprint(blueprint=blue)