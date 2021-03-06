class Config:
    # flask项目配置文件
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:itcast@127.0.0.1:3306/flaskstu'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

class DevelopmentConfig(Config):
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False