from apps.user.view import user_bp
from exts import db, api
from settings import DevelopmentConfig
from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(DevelopmentConfig)
    db.init_app(app=app)
    api.init_app(app=app)
    app.register_blueprint(user_bp)
    print(app.url_map)
    return app
