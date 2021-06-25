from sqlalchemy import create_engine, Column, Integer, String, DATE, DECIMAL, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import sessionmaker, relationship, backref

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


# 身份证表
class Id_Card(Base):
    __tablename__ = 't_id_card'
    card_number = Column(String(18), primary_key=True)
    p_id = Column(Integer, ForeignKey('t_person.id'))
    # 表示身份证对应的人
    person = relationship('Person', backref=backref('id_card', uselist=False))


# 第一种写法，使用uselist=False 不是一个列表，加在没有外键的对象中
# 第二种写法，使用backref,在主表关系中不需要维护关联属性，只要在从表中进行关联关系的维护
class Person(Base):
    # 表名
    __tablename__ = 't_person'
    id = Column(name='id', type_=Integer, primary_key=True, autoincrement=True)
    name = Column(name='name', type_=String(255))
    age = Column(name='age', type_=Integer)
    address = Column(name='address', type_=String(255))
    country = Column(type_=String(50))
    city = Column(type_=String(50))

    # 表示身份证对应的人
    # id_card = relationship('Id_Card', uselist=False)

    def __str__(self):
        return f'Emp:编号：{self.id}, 姓名：{self.name}, 年龄：{self.age},城市：{self.country}'


#
# Base.metadata.drop_all()
# Base.metadata.create_all()

# 添加数据
# d1 = Dept(d_name='研发部', city='广东')
# e1 = Emp(e_name='李梅', job='总经理', hire_data=datetime.now(), sal='55555.5554545', dept_no='1')
#
# # 创建session
session = sessionmaker(engine)()


# session.add(e1)
# session.commit()
def save_p():
    p1 = Person(name='李四', age=45)
    p2 = Person(name='王五', age=14)
    session.add_all([p1, p2])
    session.commit()


def save():
    c1 = Id_Card(card_number='10001', p_id=1)
    c2 = Id_Card(card_number='10002', p_id=2)
    session.add_all([c1, c2])
    session.commit()


def query():
    # c = session.query(Id_Card).filter(Id_Card.card_number == '10001').first()
    # print(c)
    # print(c.person.name)
    # print(c.person.age)
    p = session.query(Person).filter(Person.id == 1).first()
    print(p.id, p.name, p.id_card.card_number)


def update():
    # 第一种修改方式
    card = session.query(Id_Card).filter(Id_Card.p_id == '2').first()
    card.p_id = 3
    # 第二种修改方式
    p = session.query(Person).filter(Person.id == '3').first()
    card.person = p
    # 提交
    session.commit()


if __name__ == '__main__':
    update()
