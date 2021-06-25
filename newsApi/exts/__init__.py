from flask_caching import Cache
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# 数据库对象
db = SQLAlchemy()
# 跨域处理
cors = CORS()
# 缓存
cache = Cache()
