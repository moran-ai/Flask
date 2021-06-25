

# Flask基础

# 一. SQLAlchemy Flask连接数据库

### 1.安装SQLAlchemy

```python
pip install SQLAlchemy
```

### 2.SQLAlchemy的基本使用

#### 1.配置数据库的连接

```python
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'msbtest'
USERNAME = 'root'
PASSWORD = 'itcast'
# DB_URI='mysql+驱动名://用户名:密码@主机：端口/数据库名'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'
```

#### 2.创建数据库的引擎

```python
from sqlalchemy importr create_engine
engine = create_engine(DB_URI)
```

#### 3.测试数据库连接

```python
# 能够输出1代表连接成功
with engine.connect() as cn:
    res = cn.execute('select 1')
    print(res.fetchone())
```

#### 4.创建类，用来映射为数据表 创建ORM映射

首先需要创建一个基类Base

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base(engine)

# 创建一个类 用来映射为数据表
class Person(Base):
    # 表名
    __tablename__ = 't_person'
    id = Column(name='id', type_=Integer, primary_key=True, autoincrement=True)
    name = Column(name='name', type_=String(255))
    age = Column(name='age', type_=Integer)
    address = Column(name='address', type_=String(255))
    country = Column(type_=String(50))
    city = Column(type_=String(50))

# 创建表
Base.metadata.create_all()
# 在类中新增了数据之后，需要先删除之前的数据表，然后重新进行数据表的创建
Base.metadata.drop_all()
Base.metadata.create_all()
```

#### 5.创建ORM自动映射

需要导入自动映射的模块

```python
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'msbtest'
USERNAME = 'root'
PASSWORD = 'itcast'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'

# 创建数据库的引擎
engine = create_engine(DB_URI)

# 创建自动映射
Base = automap_base()
# 进行自动映射
Base.prepare(engine, reflect=True)
# 获取表的所有的映射类
tables = Base.Classes.keys()

# 重新定义表的名字
Person = Base.classes.t_person

# 得到当前类中所有的属性
keys = Person.__table__.columns.keys()
print(keys)
```

#### 6.数据表的增删改查

增加数据：

​	session.add()  添加一条数据

​	session.add_all([])  添加多条数据，传入一个列表

删除数据:

​	session.delete(待删除的数据)  待删除的数据需要在数据库中进行查询

修改数据：

​	① 首先需要查询待修改的数据

​    ②  待修改的数据.字段名 = 新的值

​	③ 进行提交

查找数据：	

​	session.query(类名).filter(条件).first()  第一条数据

​	session.query(类名).filter(条件).all()  多条数据

​	session.query(类名).all()  不加条件的查询

```python
from sqlalchemy import create_engine, Column, Integer, String, and_, or_, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
```

#### 7.数据表的外键关联

```python
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

# 创建一个基类 这个是所有ORM的超级父类
Base = declarative_base(engine)
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

# 添加数据
e1 = Emp(e_name='李四', job='经理', hire_data=datetime.now(), sal='55555.5554545', dept_no='1')

# 创建session
session = sessionmaker(engine)()
session.add(e1)
session.commit()
```

#### 8.数据表的一对多关联

```python
from sqlalchemy import create_engine, Column, Integer, String, DATE, DECIMAL, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import sessionmaker, relationship

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
class Dept(Base):
    __tablename__ = 't_deptno'
    dept_no = Column(Integer, primary_key=True, autoincrement=True)
    # 名字
    d_name = Column(String(255))
    city = Column(String(255))
    # 当前部门下所有员工的列表 这种写法不是最优的，最优的写法是在一个从表进行关联即可
    # emp = relationship('Emp')  # 参数是与之相关联的类名


# 员工表
class Emp(Base):
    __tablename__ = 't_emp'
    emp_no = Column(Integer, primary_key=True, autoincrement=True)
    e_name = Column(String(255))
    job = Column(String(50))
    hire_data = Column(DATE())
    # DECIMAL双精度浮点数 参数一：数据的长度，参数二：保留的小数位
    sal = Column(DECIMAL(10, 2))
    # 关联外键  ondelete；定义删除的方式
    dept_no = Column(Integer, ForeignKey('t_deptno.dept_no', ondelete='NO ACTION'))
    dept = relationship('Dept', backref='emp')  # backref代表反向访问的属性名

    def __str__(self):
        return f'Emp:员工编号：{self.emp_no}, 员工姓名：{self.e_name}, 员工职位：{self.job},员工薪资：{self.sal}'
 # # 创建session
session = sessionmaker(engine)()
# session.add(e1)
# session.commit()

# 查询数据
d = session.query(Dept).first()
for _ in d.emp:
    print(_)
```

#### 9.数据表的一对一关联

一对一关联，外键可以加在任意一个对象上面  需要添加relationship 关联，这种关联的添加可以添加在添加了外键的数据表中

一对一关联的实现方式：

​	① 使用uselist=False。这个变量值需要添加到relationship中，并且这个relationship需要添加在**主表**中

eg: 

​	id_card = relationship('Id_Card', uselist=False)

② 使用backref方法，这个方法需要进行导入,这个方法添加在**从表**的relationship中

eg:

​	person = relationship('Person', backref=('id_card', uselist=False))

```python
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

# 创建一个基类 这个是所有ORM的超级父类
Base = declarative_base(engine)

# 身份证表
class Id_Card(Base):
    __tablename__ = 't_id_card'
    card_number = Column(String(18), primary_key=True)
    p_id = Column(Integer, ForeignKey('t_person.id'))
    # 表示身份证对应的人  第二种的写法，表示一对一的关联属性
    person = relationship('Person', backref=('id_card', uselist=False))

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
   #  id_card = relationship('Id_Card', uselist=False)

    def __str__(self):
        return f'Emp:编号：{self.id}, 姓名：{self.name}, 年龄：{self.age},城市：{self.country}'
    
# 进行数据的修改
def update():
    # 第一种修改方式
    card = session.query(Id_Card).filter(Id_Card.p_id == '2').first()
    card.p_id = 3
    # 第二种修改方式
    p = session.query(Person).filter(Person.id == '3').first()
    card.person = p
    # 提交
    session.commit()
```

#### 10.数据表的多对多关系

1.创建一个中间表【必须】

用来关联其他表

创建中间表的格式：  Base.metadata：继承Base  Table需要从sqlalchemy中进行导入

​	中间表的变量名  = Table('中间表的名字'， Base.metadata, Column('联合主键1的名字', 数据类型, 外键,设置为主键))

eg:

​	 Column('s_id', Integer, ForeignKey('t_student.id'), primary_key=True)

```python
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
```

#### 11.数据库的排序

order_by:排序  desc:按照降序进行排列，默认是升序   limit:分页，每页最多展示多少条数据  offset: 从第n条开始 

##### 排序

```python
# 第一种排序,直接在query时加入order_by函数  默认是升序排列  这种排序用的最多
lst = session.query(Student).order_by(Student.age).all()
# 降序排列 desc
lst = session.query(Student).order_by(Student.age.desc()).all()
```

##### 分页和过滤

```python
lst = session.query(Student).order_by(Student.age).offset(3).limit(10).all()
for l in lst:
    print(l)
```

##### 切片

```python
lst = session.query(Student).order_by(Student.age).slice(2, 8).all()
print(lst)
```

#### 12.模糊查询

​		 模型类.query.filter(模型类.字段名.startswith('xxx')).all() 查询从xxx开头的所有数据
​        模型类.query.filter(模型类.字段名.startswith('xxx')).first() 查询从xxx开头的第一条数据
​        模型类.query.filter(模型类.字段名.endswith('xxx')).all() 查询从xxx结尾的所有数据
​        模型类.query.filter(模型类.字段名.endswith('xxx')).first() 查询从xxx结尾的第一条数据
​        模型类.query.filter(模型类.字段名.contains('xxx')).all() 查询包含xxx的所有数据
​        模型类.query.filter(模型类.字段名.like('xxx%')).all() 查询xxx开头的的所有数据
​        模型类.query.filter(模型类.字段名.like('%xxx')).all() 查询xxx结尾的的所有数据
​        模型类.query.filter(模型类.字段名.like('%xxx%')).all() 查询包含xxx的的所有数据

```python
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
```

#### 13.多条件查询

      多条件查询:
           a. or查询:
            导入or_包 from sqlalchemy import or_
            # 查询xxx开头或者包含xxx的所有数据
            模型类.query.filter(or_(模型类.字段名.like('xxx%'), 模型类.字段名.contains('xxx'))).all()
    
           b.and查询：
            from sqlalchemy import and_
            # 查询包含xxx并且大于xxx的所有数据   __gt__等效于 >  __lt__等效于 < __ge__等效于>= __le__等效于<=
            __gt__ __lt__  __ge__ __le__ 通常应用在范围（日期，时间）
            模型类.query.filter(and_(模型类.字段名.contains('xxx%'), 模型类.字段名 > 'xxxx')).all()
    
           c.not查询
            from sqlalchemy import not_
            查询不包含xxx的所有数据
            模型类.query.filter(not_(User.username.contains('xxx'))).all()
    
           d.int_查询
            查询xxx所指向的用户
            模型类.query.filter(User.phone.in_(['xxx', 'xxx'])).all()
```python
# 查询以n开头或者包含i的所有数据 or查询
lst = session.query(Student).filter(or_(Student.name.like('n%'), Student.name.contains('i'))).all()
# 查询以n开头，并且年龄大于50的所有数据  and查询
lst = session.query(Student).filter(and_(Student.name.like('n%'), Student.age > 50)).all()
# 查询不包含n的所有数据
lst = session.query(Student).filter(not_(Student.name.contains('n'))).all()
# in_指向具体的数据
lst = session.query(Student).filter(Student.name.in_(['lisi', 'wangwu'])).all()
```

#### 14.通过主键进行查询

模型类.query.get(主键)  根据主键查询

```python
stu_id = session.query(Student).get(i)
```

#### 15.懒加载

懒加载：查询数据时，不需要查询所有的数据，只需要获取指定的数据，提高效率

懒加载可以进行数据的追加，排序以及过滤

在使用了懒加载以后，对象会返回一个AppenderQuery()对象，然后可以利用这个AppenderQuery()进行数据的追加，排序以及过滤

在执行sql语句时，只有调用了first()方法和all()方法，sql才会被执行

在Flask框架中的具体实现：

​	① 在backref中加入一个参数lazy='dynamic',lazy的默认值是select 

​		relationship('Dept', backref=backref('emp', lazy='dynamic'))

​	② 得到一个AppenderQuery对象

​		# 编写一个sql语句

​		d = session.query(Dept).filter(Dept.dept_no == 1)

​		执行一个sql语句，调用first()方法

​		result = d.first()  # 返回一个AppenderQuery()对象  这个对象可以进行数据的追加，排序和过滤

​	③ 追加一条数据  使用append()方法

​	 #  首先创建一条数据

​		e = Emp(e_name='里么', job='mananger', hire_data=datetime.now(), sal='4545453.34535435', dept_no=1)

​		# 调用append方法

​		result.emp.append(e)



​		④ 使用filter()方法进行过滤

​		# 进行过滤

​		result.emp.filter(Emp.emp_no > 6).all()
​		session.commit()

##### 16.分组和过滤以及子查询

分组:groupy_by

过滤：having 用在分组后面  func.count() 需要进行导入

子查询：subquery()

分组的格式：session.query(类名.字段名, func.count(类名.字段名)).groupy_by(类名.字段名).all()

```python
session.query(Emp.sal, func.count(Emp.emp_no)).group_by(Emp.sal).all()
```

过滤的格式: session.query(类名.字段名, func.count(类名.字段名)).groupy_by(类名.字段名).having(过滤的条件).all()

```python
session.query(Emp.sal, func.count(Emp.emp_no)).group_by(Emp.sal).having(Emp.sal > 3000).all()
```

子查询的格式：session.query(类名.字段名.label('别名'), 类名1.字段名.label('别名')).filter(过滤的条件).subquery()  

label:给字段名加上别名  filter: 进行条件的筛选

```python
e = session.query(Emp.hire_data.label('h_d'), Emp.job.label('job')).filter(Emp.e_name == '李四').subquery()
```

父查询的格式： session.query(类名).filter(类名.字段名==子查询的变量接收名字.c.子查询字段的别名, 类名.字段名==子查询变量的接收名字.c.子查询字段的别名).all()

c： 代表从子查询中进行数据的获取

```python
session.query(Emp).filter(Emp.hire_data == e.c.h_d, Emp.job == e.c.job).all()
```





# 二.flask_sqlalchemy连接数据库

flask_sqlalchemy是在sqlalchemy的基础上进行了优化

### 1.安装flask_sqlalchemy

```python
pip install flask-sqlalchemy
```

### 2.配置flask_sqlalchemy

app.py文件

 ① 导入sqlalchemy

```python
from flask_sqlalchemy import  SQLAlchemy
```

② 进行配置sqlalchemy

```python
# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'msbtest'
USERNAME = 'root'
PASSWORD = 'itcast'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
```

③ 创建模型

```python
db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(40))
    password = db.Column(db.String(255))
	
    # 定义输出格式
    def __repr__(self):
        return f'用户编号：{self.id} ---> 用户名：{self.uname} ---> 密码: {self.password}'
```

④ 创建数据表

db.create_all()

如果对数据表进行了更改，则需要删除数据表，然后将新的表进行创建

db.drop_all()

db.create_all()

### 使用alembic进行数据表的创建以及迁移

安装alembic

```python
pip install alembic
```

alembic安装完成以后，需要创建数据表,可以直接在app.py文件中进行数据表的创建

```python
import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 't_user_1'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(40))
    password = db.Column(db.String(255))
    address = db.Column(db.String(50))

    def __repr__(self):
        return f'用户编号：{self.id} ---> 用户名：{self.uname} ---> 密码: {self.password}'


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
```

数据表创建之前，设置配置文件config.py

```python
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'msbtest'
USERNAME = 'root'
PASSWORD = 'itcast'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

进行初始化

alembic init 自定义文件名

```
alembic init my_alembic
```

初始化完成以后会生成几个文件

​	一个文件是：alembic.ini

​	一个文件夹是：my_alembic

进行文件的修改：

​		首先修改alembic.ini文件里的sqlalchemy.url的值

```
sqlalchemy.url = mysql+pymysql://root:itcast@127.0.0.1:3306/msbtest
```

进行文件夹中文件的修改，修改其中的env.py文件

将其中的target_metadata进行修改，这是项目的位置,修改之前需要将当前项目临时加载到环境变量中

```python
import os
import sys

# 当前项目加入到path中【临时】
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import app

# target_metadata = None
target_metadata = app.db.Model.metadata  # 模型的位置
```

上面的文件修改完成之后，开始进行数据库的迁移

-m后面的内容可以进行自定义

```
alembic revision --autogenerate -m first 
```

将数据真正迁移到数据库

```
alembic upgrade head 
```

如果对数据表有修改，只要重复执行上面的两条语句即可

### 使用flask_migrate, flask_script进行数据表的创建以及迁移

安装：

```base
pip install flask-migrate  发布命令
pip install flask-script   管理命令
pip install flask-bootstrap 
```

配置flask settings.py

```python
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
```



配置app

创建一个单独的文件夹apps，用来创建app

```python
from flask import Flask
from settings import DevelopmentConfig
from ext import db, bootstrap
from ym import ym_bp
from models.User import User

def create_app():
    app = Flask(__name__)
    # 配置开发者环境
    app.config.from_object(DevelopmentConfig)
    # 配置数据库
    db.init_app(app)
    # 配置bootstrap
    bootstrap.init_app(app)
    # 注册蓝图
    app.register_blueprint(ym_bp)
    return app
```

编写app.py文件

```python
from ext import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from models.User import User
from apps import create_app

app = create_app()

manager = Manager(app=app)
# 影响数据库的映射
migrate = Migrate(app=app, db=db)
# 将命令交给manager进行管理
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
```

创建蓝图

```python
from flask import Blueprint

ym_bp = Blueprint('/ym', __name__, url_prefix='/ym')
```

注册蓝图

```python
 app.register_blueprint(ym_bp)
```

创建模型

```python
from ext import db


# 创建用户表
class User(db.Model):
    __tablename__ = 't_user_img'
    u_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 名字不能为空
    name = db.Column(db.String(40), nullable=False)
    # 密码不能为空
    passwword = db.Column(db.String(15), nullable=False)
    # 邮箱
    email = db.Column(db.String(50))
    # 手机号 unique=True 手机号唯一
    phone = db.Column(db.String(11), unique=True)
```

进行初始化

在终端运行相关命令

```
python app.py db init  产生一个migrations文件夹，每个项目只需要一次
```

```
python app.py db migrate  进行迁移 记录对数据表的修改
```

```
python app.py db upgrade 进行数据的同步 真正同步到了数据库
```

如果前面的迁移同步发生了错误，可以进行降级

```
python app.py db downgrade 
```

# 三.RESTFUL编程

1.每个url代表一种资源

2.客户端使用GET，POST,PUT,DELETE方式对资源进行操作

GET:获取资源

POST:新建资源或者更新资源

PUT:更新资源

DELETE:删除资源

3.通过资源的表现形式来操作资源

4.资源的表现形式的是XML或者JSON

5. 安装：

```python
pip install flask-restful
```

##### 在普通的app上创建一个api

创建一个API

```python
from flask_restful import Resource, Api
app = Flask(__name__)
# 对外提供一个接口。可以访问某个资源
api = Api(app=app)
```

创建一个资源，继承Resource

```python
# 定义一个资源
class HelloResource(Resource):
    def get(self):
        return {'get': '获取资源'}

    def post(self):
        return {'post': '新建或者更新资源'}

    def put(self):
        return {'put': '更新资源'}

    def delete(self):
        return {'delte': '删除资源'}
```

资源绑定api

```python
# 资源绑定api
api.add_resource(HelloResource, '/hello')
```

##### 在蓝图上使用api

导入蓝图和Api以及Resource模块

```python
from flask import Blueprint
from flask_restful import Resource, Api
```

创建蓝图

```python
user_bp = Blueprint('user', __name__)
```

给蓝图提供一个接口

```python
api = Api(user_bp)
```

创建一个资源,这个资源同样需要继承Resource这个父类

```python
class HelloResource(Resource):
    def get(self):
        return {'get': '获取资源'}

    def post(self):
        return {'post': '新建或者更新资源'}

    def put(self):
        return {'put': '更新资源'}

    def delete(self):
        return {'delte': '删除资源'}
```

进行资源的绑定

```python
api.add_resource(HelloResource, '/hello')
```

这里的蓝图需要注册到app中，但是不能在代码开始进行注册，如果在代码进行了注册，那么就将蓝图注册到了当前的文件上，对后面的内容进行了覆盖

所以在这里，将蓝图注册到代码的后面，或者新建一个独立的文件，用来存放app文件，这里在代码的最后进行蓝图的注册

```python
app.register_blueprint(user_bp, url_prefix='/user')
```

##### 参数校验

安装

```python
pip install flask-restful
```

导入相关依赖包

```python
from flask_restful import Resource, Api, reqparse, inputs 
# inputs模块用来进行类型的确定，比如范围，正则匹配，自然数匹配 reqparse是进行校验的
from flask import Flask
```

定义一个资源，并定义四种方法[GET,POST,PUT,DELETE], 并进行参数的校验

```python
class HelloResource(Resource):
    def get(self):
        return {'get': '获取资源'}
    
    def  post(self):
    	return {"post": '新建资源或者修改资源'}
    
        def put(self):
        return {'put': '更新资源'}

    def delete(self):
        return {'delte': '删除资源'}
```

在post方法中进行参数的校验

首先需要创建一个参数校验的对象

```python
rq = reqparse.RequestParser()
```

加入参数，并对 参数进行校验，使用add_argument方法添加参数，required=True表示该参数为必填项,help为错误信息，type为类型

调用inputs函数进行范围，正则的类型的确定

使用location属性确定提交的方式

form为表单提交

```python
 # ② 定义参数的定义声明  required=True必填项
rq.add_argument('a', required=True, help='参数a错误', type=int)  # 如果定义了help，所有的错误提示都会是同一个提示
# action='append' 获取多个同名变量的值  默认获取第一个同名变量的值
rq.add_argument('b', required=True, type=str, action='append')  # 如果定义了help，所有的错误提示都会是同一个提示
# choices 参数规定的范围  参数只能选择choices里面的值
rq.add_argument('c', required=True, type=str, choices=['男', '女'])  # 如果定义了help，所有的错误提示都会是同一个提示
# 只允许两位数的整数，使用正则表达式
rq.add_argument('d', required=True, type=inputs.regex('^\d{2}$'))  # 如果定义了help，所有的错误提示都会是同一个提示
# 确定范围，只允许1到100的整数，包括1和100
rq.add_argument('e', required=True, type=inputs.int_range(1, 100))  # 如果定义了help，所有的错误提示都会是同一个提示
# 只允许传递boolean值  location：提交的位置  form为表单提交
rq.add_argument('f', required=True, type=inputs.boolean, location='form')  # 如果定义了help，所有的错误提示都会是同一个提示
```

```python
parser.add_argument('name', type=int, location='form')
# Look only in the querystring
parser.add_argument('PageSize', type=int, location='args')
# From the request headers
parser.add_argument('User-Agent', location='headers')
# From http cookies
parser.add_argument('session_id', location='cookies')
# From json
parser.add_argument('user_id', location='json')
# From file uploads
parser.add_argument('picture', location='files')
```

也可以指定多个位置

```python
parser.add_argument('text', location=['headers', 'json'])
```

开始进行参数的校验

参数校验的函数有返回值，使用一个变量进行接收  使用参数校验对象中的parse_args()方法

```python
req = rq.parse_args()
```

校验完成后取得校验之后值

```python
a = req.a
b = req.b
c = req.c
d = req.d
e = req.e
f = req.f
```

返回一个json格式的数据，将校验通过的参数添加进去

```python
return {'post': '新建或者更新资源', 'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f}
```

进行资源的绑定

```python
api.add_resource(HelloResource, '/hello')
```

##### 处理序列化数据[json]

首先需要定义一个app和一个api接口

然后定义一个模型User

```python
# 定义一个模型类
class User(object):
    def __init__(self, user_id, password, username):
        self.user_id = user_id
        self.password = password
        self.user_name = username
```

需要将这个模型类转为一个序列化数据，使用fields定义格式

```python
property_fields = {
    'user_name': fields.String,
    'password': fields.String
}
```

从json.py的源码文件中，将所有的源代码拿过来, from __future__ import absolute_import这行去掉，然后自定义一个message

加上装饰器@api.representation('application/json')用来指定响应的类型为json

```python
from flask import make_response, current_app
from flask_restful.utils import PY3
from json import dumps
@api.representation('application/json')
def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""
    # 自定义一些内容
    if not 'message' in data:
        data = {
            'message': 'OK',
            'data': data
        }
    settings = current_app.config.get('RESTFUL_JSON', {})

    # If we're in debug mode, and the indent is not set, we set it to a
    # reasonable value here.  Note that this won't override any existing value
    # that was set.  We also set the "sort_keys" value.
    if current_app.debug:
        settings.setdefault('indent', 4)
        settings.setdefault('sort_keys', not PY3)

    # always end the json dumps with a new line
    # see https://github.com/mitsuhiko/flask/pull/1262
    dumped = dumps(data, **settings) + "\n"

    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp
```

定义一个资源，继承Resource

在get方法中，使用装饰器marshal_with(自定义的格式)或者函数marshal(自定义的格式)将模型转为序列化数据

marshal_with和marshal需要从flask_restful进行导入

```python
class HelloResource(Resource):
    # 使用自定义的格式
    @marshal_with(property_fields)
    def get(self):
        u = User(1, '李梅', '123456')
        # return marshal(u, property_fields,envelope='data1')
        return u

    def post(self):
        return {'post': '新建或者更新资源'}

    def put(self):
        return {'put': '更新资源'}

    def delete(self):
        return {'delte': '删除资源'}
```

资源绑定接口，并启动

```python
api.add_resource(HelloResource, '/hello')

if __name__ == '__main__':
    app.run(debug=True)
```

