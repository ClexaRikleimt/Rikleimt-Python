from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle

app = Flask(__name__)
db = SQLAlchemy(app)  # TODO: Do this the nice way and move it to a separate file, then use init_app() [Arlena]

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('scss/app.scss', filters='pyscss', depends='scss/**/*.scss', output='css/app.css')
js_vendor = Bundle(
    'bower_components/jquery/dist/jquery.min.js',
    'bower_components/bootstrap/dist/js/bootstrap.min.js',
    output='js/vendor.js')
css_vendor = Bundle(
    'bower_components/bootstrap/dist/css/bootstrap.min.css',
    output='css/vendor.css'
)

assets.register('scss_app', scss)
assets.register('js_vendor', js_vendor)
assets.register('css_vendor', css_vendor)


from rikleimt.views import Index

app.add_url_rule('/', Index.endpoint, view_func=Index.as_view(Index.endpoint), methods=['GET'])


if __name__ == '__main__':
    app.run()
