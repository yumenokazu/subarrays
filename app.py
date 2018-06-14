from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    return app


app = create_app()
from views import *

if __name__ == '__main__':
    app.run()

