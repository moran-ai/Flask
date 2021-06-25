from datetime import datetime

from exts import db

class User(db.Model):
    # autoincrement = True 自增
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(11))
    icon = db.Column(db.String(200))
    isdelete = db.Column(db.Boolean())
    email = db.Column(db.String(100))
    udatetime = db.Column(db.DateTime, default=datetime.now)
    # friends = db.relationship('Friend', backref='user')

class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 当前用户id
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 朋友
    fid = db.Column(db.Integer, db.ForeignKey('user.id'))
