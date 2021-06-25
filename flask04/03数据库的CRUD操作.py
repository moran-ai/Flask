"""
数据库的增删改查
"""
from sqlalchemy import create_engine, Column, Integer, String, and_, or_, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

    def __str__(self):
        return f'Person:[id:{self.id}, name: {self.name}, age:{self.age}, address:{self.address}, country:{self.country}, city:{self.city}]'


# 创建session  sessionmaker 返回一个函数，需要进行调用加入一个()
session = sessionmaker(engine)()


# 添加对象，也就是添加数据
def save():
    p1 = Person(name='李梅', age=23, address='北京-海定区', country='中国', city='北京')
    p2 = Person(name='李四', age=24, address='深圳-福田区', country='中国', city='广东')
    p3 = Person(name='王五', age=25, address='四川-成都', country='中国', city='四川')
    session.add_all([p2, p3])
    session.commit()


# 查找数据
def query():
    p = session.query(Person).first()
    # print(p)
    # 查询年龄在18岁以上的  打印sql语句，如果加上first或者all返回一个具体的数据
    query_list = session.query(Person).filter(Person.age > 18).all()
    print(query_list)

    # 查询年龄在18岁以上，48以下
    # 第一种写法
    query_list1 = session.query(Person).filter(and_(Person.age > 18, Person.age < 48)).all()
    # 第二种写法
    query_list1 = session.query(Person).filter(Person.age > 18, Person.age < 48).all()
    print(query_list1)

    # 查询所有年龄大于18的人数
    result = session.query(func.count(Person.id)).filter(Person.age > 18).first()
    print(result)


# 修改数据
def update():
    p = session.query(Person).filter(Person.id == 1).first()
    print(p.age)
    p.age = 60
    session.commit()


# 删除数据
def delete():
    p = session.query(Person).filter(Person.id == 2).first()
    session.delete(p)
    session.commit()


if __name__ == '__main__':
    delete()
