from flask import Flask, Blueprint

# 创建蓝图对象
user_bp = Blueprint('user', __name__)


@user_bp.route('/say')
def say_user():
    return 'hello word'
