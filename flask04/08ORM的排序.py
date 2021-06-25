import random
from sqlalchemy import create_engine, Column, Integer, String, DATE, DECIMAL, ForeignKey, Table, or_, not_, and_
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

    # __mapper_args__ = {
    #     'order_by': age.desc()
    # }


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
    students = []
    for i in range(10):
        s = Student(name=f'name-{i}', age=random.randint(1, 100))
        students.append(s)
    session.add_all(students)
    session.commit()


def query():
    # 第一种排序,直接在query时加入order_by函数  默认是升序排列
    lst = session.query(Student).order_by(Student.age).all()
    # 降序排列 desc
    lst = session.query(Student).order_by(Student.age.desc()).all()

    # 第二种排序
    lst = session.query(Student).all()
    print(lst)


def update():
    pass


def page_query():
    """
    limit函数 最多可以取n条数据
    offset()  从第n条开始取
    :return:
    """
    lst = session.query(Student).order_by(Student.age).offset(3).limit(10).all()
    for l in lst:
        print(l)


def page_query_1():
    """
    切片 slice
    截取第三条数据到第8条数据中之间的数据  不包含第3条数据，包含第8条数据  左开右闭
    :return:
    """
    lst = session.query(Student).order_by(Student.age).slice(2, 8).all()
    print(lst)


def page_query_():
    """
    模糊查询数据
    :return:
    """
    # 查询以n开头的所有数据
    lst = session.query(Student).filter(Student.name.startswith('n')).all()
    # 查询以n开头的第一条数据
    lst = session.query(Student).filter(Student.name.startswith('n')).first()
    # 查询以n结尾的所有数据
    lst = session.query(Student).filter(Student.name.endswith('n')).all()
    # 查询以n结尾的第一条数据
    lst = session.query(Student).filter(Student.name.endswith('n')).first()
    # 查询包含n的所有数据
    lst = session.query(Student).filter(Student.name.contains('n')).order_by(Student.age).all()
    # 查询以n开头的数据
    lst = session.query(Student).filter(Student.name.like('n%')).all()
    # 查询包含n的数据
    lst = session.query(Student).filter(Student.name.like('%n%')).all()
    # 查询以i结尾的数据
    lst = session.query(Student).filter(Student.name.like('%i')).all()
    for i in lst:
        print(i)


def all_query():
    """
    多条件查询
    :return:
    """
    # 查询以n开头或者包含i的所有数据 or查询
    lst = session.query(Student).filter(or_(Student.name.like('n%'), Student.name.contains('i'))).all()
    # 查询以n开头，并且年龄大于50的所有数据  and查询
    lst = session.query(Student).filter(and_(Student.name.like('n%'), Student.age > 50)).all()
    # 查询不包含n的所有数据
    lst = session.query(Student).filter(not_(Student.name.contains('n'))).all()
    # in_指向具体的数据
    lst = session.query(Student).filter(Student.name.in_(['lisi', 'wangwu'])).all()
    for i in lst:
        print(i)


def get_primary():
    for i in range(10):
        stu_id = session.query(Student).get(i)
        print(stu_id)

if __name__ == '__main__':
    # save_p()
    # pass
    get_primary()
    # save()
    # pass
