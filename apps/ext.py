from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class

db = SQLAlchemy()

migrate = Migrate()


# ========数据库相关配置 start=========

def init_db(app):
    init_config(app)

    init_uploads(app)

    db.init_app(app)

    migrate.init_app(app=app, db=db)


def init_config(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@127.0.0.1:3306/flask_trip'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


# ========数据库配置end=========


# ========文件上传相关配置 start=========
# 配置路径
import os

# 获取当前文件所在根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 获取当前根目录下文件上传的目录
UPLOAD_PATH = os.path.join(BASE_DIR, 'static/upload/')
# 文件上传核心类
images_upload = UploadSet('images', extensions=IMAGES)


def init_uploads(app):
    # 配置文件上传的根目录 ctrl+shift+u 把所有小写字母转化成大写
    app.config['UPLOADS_DEFAULT_DEST'] = UPLOAD_PATH
    app.config['UPLOADS_DEFAULT_URL'] = 'http://127.0.0.1:8000/static/upload'

    # 配置文件上传的类型
    configure_uploads(app, images_upload)
    # 配置上传文件的最大值
    patch_request_class(app, 16 * 1024 * 1024)

# ========文件上传end============
