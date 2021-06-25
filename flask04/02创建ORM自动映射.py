from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base

# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'msbtest'
USERNAME = 'root'
PASSWORD = 'itcast'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'

# 创建数据库引擎
engine = create_engine(DB_URI)

# 创建自动映射  自动映射表名和类名一致
Base = automap_base()
# 进行映射
Base.prepare(engine, reflect=True)

# 获取所有表的映射类
tables = Base.classes.keys()
# print(tables)

# 重新定义表的名字
Person = Base.classes.t_person

# 得到当前类中所有的属性
keys = Person.__table__.columns.keys()
print(keys)
