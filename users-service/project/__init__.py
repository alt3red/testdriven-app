import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


# instantiate the db
db = SQLAlchemy()

def create_app():
    
    # instanciate the app
    app = Flask(__name__)

    # set config
    app.settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app.settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    return app
