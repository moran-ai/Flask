from datetime import datetime

from exts import db

class User(db.Model):
    # primary_key=True 主键  autoincrement=True 自增
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # nullable=False 不允许为空
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    # unique=True 唯一
    phone = db.Column(db.String(11), unique=True)
    # default 默认值
    rdatetime = db.Column(db.DateTime, default=datetime.now)
    # 逻辑删除
    isdelete = db.Column(db.Boolean, default=False)

    def __str__(self):
        return self.username

