from flask import Blueprint, render_template

from apps.home.models import Destination, Photo

home = Blueprint('home', __name__, static_folder='static')


@home.route('/')
def login():
    return render_template('home.html')


@home.route('/home/list/<int:page>/<int:size>/')
def list(page, size):
    paginate = Destination.query.paginate(page=page, per_page=size, error_out=False)
    return render_template('index.html', paginate=paginate)


@home.route('/home/photo/')
def show_photo():
    photos = Photo.query.filter(Photo.des_id)
    return render_template('detail.html', photos=photos)


@home.route('/123/')
# 原生态的css样式
def index():
    return render_template('temp1.html')
