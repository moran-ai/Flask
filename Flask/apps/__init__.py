from flask import Flask
from apps.user.view import user_bp
import settings
from ext import db

def create_app():
    # app是一个核心对象
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings.DevelopmentConfig)  # 加载配置

    # 注册蓝图
    app.register_blueprint(user_bp)  # 将蓝图对象与app绑定，使用register_blueprint(蓝图对象)函数
    # print(app.url_map)

    # 将db对象与app进行关联
    db.init_app(app)

    return app
