from sqlalchemy import create_engine, Column, Integer, String, DATE, DECIMAL, ForeignKey, func
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


# 部门和员工 一对多
# 部门表
class Dept(Base):
    __tablename__ = 't_deptno'
    dept_no = Column(Integer, primary_key=True, autoincrement=True)
    # 名字
    d_name = Column(String(255))
    city = Column(String(255))

    # 当前部门下所有员工的列表 这种写法不是最优的，最优的写法是在一个从表进行关联即可
    # emp = relationship('Emp')  # 参数是与之相关联的类名
    def __repr__(self):
        return f'部门编号：{self.dept_no},部门名称:{self.d_name}'


# 员工表
class Emp(Base):
    __tablename__ = 't_emp'
    emp_no = Column(Integer, primary_key=True, autoincrement=True)
    e_name = Column(String(255))
    job = Column(String(50))
    hire_data = Column(DATE())
    # DECIMAL双精度浮点数 参数一：数据的长度，参数二：保留的小数位
    sal = Column(DECIMAL(10, 2))
    # 关联外键
    dept_no = Column(Integer, ForeignKey('t_deptno.dept_no', ondelete='NO ACTION'))
    # dept = relationship('Dept', backref=backref('emp', lazy='dynamic'))  # backref代表反向访问的属性名  lazy的默认值是select
    dept = relationship('Dept', backref='emp')  # backref代表反向访问的属性名  lazy的默认值是select

    def __str__(self):
        return f'Emp:员工编号：{self.emp_no}, 员工姓名：{self.e_name}, 员工职位：{self.job},员工薪资：{self.sal}'


# Base.metadata.drop_all()
# Base.metadata.create_all()

# 添加数据
# d1 = Dept(d_name='研发部', city='广东')
# e1 = Emp(e_name='李梅', job='总经理', hire_data=datetime.now(), sal='55555.5554545', dept_no='1')
#
# # 创建session
session = sessionmaker(engine)()


def test_lazy():
    # 进行分组
    e = session.query(Emp.sal, func.count(Emp.emp_no)).group_by(Emp.sal).all()
    # print(e)

    #  统计每个工资级别下的员工数量，只统计薪资在3000以上的员工
    resuult = session.query(Emp.sal, func.count(Emp.emp_no)).group_by(Emp.sal).having(Emp.sal > 3000).all()
    # print(resuult)


def subQuery():
    """
    子查询
    :return:
    """
    # 查询和李四入职时间以及职位相同的所有员工  label 取别名
    e = session.query(Emp.hire_data.label('h_d'), Emp.job.label('job')).filter(Emp.e_name == '李四').subquery()
    # c是用来获取子查询中的值的一个函数
    result = session.query(Emp).filter(Emp.hire_data == e.c.h_d, Emp.job == e.c.job).all()
    for i in result:
        print(i)


if __name__ == '__main__':
    subQuery()
