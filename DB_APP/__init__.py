import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from DB_APP.config import Config

# Creating SQLAlchemy Instance to work with
db = SQLAlchemy()


def create_app(config_class=Config):
    # Setting the 'templates' directory as default template-directoy for Flask App
    template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    template_dir = os.path.join(template_dir, 'templates')

    # For testing purposes
    # print(template_dir)

    app = Flask(__name__,
                template_folder=template_dir
                )
    app.config.from_object(Config)

    db.init_app(app)

    # register route-files as Blueprints to be able to import throughout the app
    from DB_APP.Main.routes import main
    app.register_blueprint(main)

    return app
