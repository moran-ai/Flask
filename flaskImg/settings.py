class Config:
    """
    Flask配置文件
    """
    DEBUG = True
    # 数据库的连接
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:itcast@127.0.0.1:3306/flaskimg'
    # 过滤警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    # 设置session会话机制机制密钥
    SECRET_KEY = 'dafadgagfasfasfszfs'


class DevelopmentConfig(Config):
    """
    设置开发环境
    """
    ENV = 'development'


class ProductionConfig(Config):
    """
    设置生产环境，项目部署后采用生产环境
    """
    DEBUG = False
    ENV = 'production'
