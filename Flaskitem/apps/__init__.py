from flask import Flask

from apps.user.view import user_bp
from exts import db
from settings import DevelopmentConfig

def creat_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    # 配置
    app.config.from_object(DevelopmentConfig)
    # 将db对象与app相关联
    db.init_app(app=app)

    # 将蓝图与app相关联,注册蓝图
    app.register_blueprint(user_bp)

    return app