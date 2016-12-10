# encoding=utf-8
from rikleimt.application import create_app
from rikleimt.views import Index


app = create_app()

app.add_url_rule('/', Index.endpoint, view_func=Index.as_view(Index.endpoint), methods=['GET'])


if __name__ == '__main__':
    app.run()
