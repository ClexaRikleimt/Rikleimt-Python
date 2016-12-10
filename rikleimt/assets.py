# encoding=utf-8
from flask import current_app
from flask_assets import Environment, Bundle


assets = Environment()

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
