from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'msbtest'
USERNAME = 'root'
PASSWORD = 'itcast'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'

# 创建数据库引擎
engine = create_engine(DB_URI)

# # 测试数据库连接
# with engine.connect() as cn:
#     res = cn.execute('select 1')
#     print(res.fetchone())

# 创建一个基类 这个是所有ORM的超级父类
Base = declarative_base(engine)


# 定义python类和表的映射
class Person(Base):
    # 表名
    __tablename__ = 't_person'
    id = Column(name='id', type_=Integer, primary_key=True, autoincrement=True)
    name = Column(name='name', type_=String(255))
    age = Column(name='age', type_=Integer)
    address = Column(name='address', type_=String(255))
    country = Column(type_=String(50))
    city = Column(type_=String(50))


# 字段种新增了数据，需要先删除数据表，在进行创建
Base.metadata.drop_all()  # 删除表
# 创建表
Base.metadata.create_all()
