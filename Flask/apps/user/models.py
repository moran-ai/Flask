# ORM  类 ----> 表
# 类对象  ----> 表中的一条记录
from datetime import datetime

from ext import db

class User(db.Model):
    """
    创建表名 User
    db.Column(数据类型, 约束(主键，是否为空)) 映射为数据库表中的列

    常用数据类型：
        1. db.Integer ---> int
        2. db.String(15) ---> varchar(15)
        3. db.Datetime ----->datetime
    """
    # 主键primary_key=True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)  # 不能为空 nullable=False
    password = db.Column(db.String(12), nullable=False)
    phone = db.Column(db.String(11), unique=True)  # unique=True 唯一
    # 注册时间  datetime.now 系统默认时间
    rdatetime = db.Column(db.DateTime, default=datetime.now)
    email = db.Column(db.String(20))

    def __str__(self):
        return self.username
