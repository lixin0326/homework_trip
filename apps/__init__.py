from flask import Flask

from apps.ext import init_db
from apps.home.views import home


def create_app():
    app = Flask(__name__)
    app.debug = True
    # 注册蓝图
    register_blue(app)
    init_db(app)
    return app


def register_blue(app):
    app.register_blueprint(home)
