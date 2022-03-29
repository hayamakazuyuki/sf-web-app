from flask import Flask

from .contractors.views import contractors

def create_app():
    app = Flask(__name__)

    app.register_blueprint(contractors)
    return app