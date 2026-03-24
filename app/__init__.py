from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.update(
        SECRET_KEY="phase3-dev-key",
        SQLALCHEMY_DATABASE_URI="sqlite:///phase3.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        APP_TITLE="Url Shortener With Analytics",
        APP_SUMMARY="Production-oriented general solution for url shortener with analytics workflows.",
        DOMAIN="General",
        ENTITY="Domain Record",
        ENTITY_PLURAL="Domain Records",
    )

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    from .routes.web import web_bp
    from .routes.api import api_bp

    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    with app.app_context():
        from . import models

        db.create_all()

    return app
