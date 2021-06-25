from flask import Blueprint

order = Blueprint('order', __name__)

from . import order_func
