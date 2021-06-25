from sqlalchemy import create_engine, Column, Integer, String, DATE, DECIMAL, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
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


# 部门和员工 一对多
# 部门表
class Dept(Base):
    __tablename__ = 't_deptno'
    dept_no = Column(Integer, primary_key=True, autoincrement=True)
    # 名字
    d_name = Column(String(255))
    city = Column(String(255))


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


# Base.metadata.create_all()

# 添加数据
# d1 = Dept(d_name='研发部', city='广东')
e1 = Emp(e_name='李四', job='经理', hire_data=datetime.now(), sal='55555.5554545', dept_no='1')

# 创建session
session = sessionmaker(engine)()
session.add(e1)
session.commit()
