from flask import Blueprint, current_app

item_bp = Blueprint('/item', __name__, url_prefix='/item')


@item_bp.route('/')
def hello():
    h = current_app.h
    print(h)
    return 'ok'
