from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def init_db(app):
    init_config(app)
    db.init_app(app)
    migrate.init_app(app=app, db=db)


def init_config(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@127.0.0.1:3306/flask_trip'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


db = SQLAlchemy()
migrate = Migrate()
