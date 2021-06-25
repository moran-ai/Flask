from sqlalchemy import create_engine, Column, Integer, String, DATE, DECIMAL, ForeignKey, Table
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

# 创建一个基类 这个是所有ORM的超级父类
Base = declarative_base(engine)

# 定义一个中间表
temp_tab = Table(
    't_temp_tab',
    Base.metadata,
    # 创建联合主键
    Column('s_id', Integer, ForeignKey('t_student.id'), primary_key=True),
    Column('c_id', Integer, ForeignKey('t_course.id'), primary_key=True)
)


# 第二步，定义两个多对多的模型对象
class Student(Base):
    __tablename__ = 't_student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(400))
    age = Column(Integer)

    # 定义关联关系
    sourse_list = relationship('Course', backref='student_list', secondary=temp_tab)

    def __repr__(self):
        return f'学生姓名：{self.name}, 学生的年龄:{self.age}'


class Course(Base):
    __tablename__ = 't_course'
    id = Column(Integer, primary_key=True, autoincrement=True)
    c_name = Column(String(60))

    def __repr__(self):
        return f'课程名是：{self.c_name}'


# 创建表
# Base.metadata.drop_all()
# Base.metadata.create_all()

# # 创建session
session = sessionmaker(engine)()


def save_p():
    s1 = Student(name='lisi', age=23)
    s2 = Student(name='wangwu', age=33)

    c1 = Course(c_name='英语')
    c2 = Course(c_name='数学')

    s1.sourse_list.append(c1)
    s1.sourse_list.append(c2)
    s2.sourse_list.append(c1)
    s2.sourse_list.append(c2)
    session.add(s1)
    session.add(s2)
    session.commit()


def save():
    pass


def query():
    # 按照学生查找课程
    stu = session.query(Student).first()
    # for s in stu.sourse_list:
    #     print(s.c_name)
    #     print(s.id)

    # 按照课程查找学生
    c = session.query(Course).first()
    for _ in c.student_list:
        print(_.name, _.age)


def update():
    pass


if __name__ == '__main__':
    # save_p()
    # pass
    query()
