# encoding=utf-8
from flask import render_template
from flask.views import View


class Index(View):
    endpoint = 'index'

    def dispatch_request(self):
        return render_template('index.html')
