from flask import Flask

from apps.ext import init_db, init_config
from apps.home.views import home
from apps.upload.views import upload


def create_app():
    app = Flask(__name__)
    app.debug = True
    # 注册蓝图
    register_blue(app)
    # 注册所有第三方配置
    init_db(app)

    return app


# 　注册蓝图模块
def register_blue(app):
    app.register_blueprint(home)
    app.register_blueprint(upload)
