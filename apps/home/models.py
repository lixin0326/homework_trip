import datetime

from apps.ext import db


class Destination(db.Model):
    des_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    des_name = db.Column(db.String(100), unique=True, index=True, nullable=False)
    price = db.Column(db.Numeric(9, 2), default=0.00, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    is_delete = db.Column(db.Boolean, default=0)

    photo_list = db.relationship('Photo',
                                 backref='destination',
                                 lazy='dynamic'
                                 )


class Photo(db.Model):
    p_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(100), unique=True, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    des_id = db.Column(db.Integer, db.ForeignKey(Destination.des_id))
