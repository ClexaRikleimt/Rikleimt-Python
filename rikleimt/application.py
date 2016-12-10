# encoding=utf-8
from flask import Flask


def create_app():
    app = Flask(__name__)

    # from rikleimt.models import db
    # db.init_app(app)
    # TODO: Uncomment when database should be running [Arlena]

    from rikleimt.assets import assets
    assets.init_app(app)
    with app.app_context():  # Weird flask-assets thingy [Arlena]
        assets.url = app.static_url_path

    return app
