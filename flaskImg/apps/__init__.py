from flask import Flask
from settings import DevelopmentConfig
from ext import db, bootstrap
from ym import ym_bp


def create_app():
    app = Flask(__name__)
    # 配置开发者环境
    app.config.from_object(DevelopmentConfig)
    # 配置数据库
    db.init_app(app)
    # 配置bootstrap
    bootstrap.init_app(app)
    # 注册蓝图
    app.register_blueprint(ym_bp)
    return app
