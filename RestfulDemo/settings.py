import os

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:itcast@127.0.0.1:3306/flaskRestful'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'qerrt24546'
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    STATIC_DIR = os.path.join(BASE_PATH, 'static')
    UPLOAD_DIR = os.path.join(STATIC_DIR, 'upload\\icon')

class DevelopmentConfig(Config):
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
