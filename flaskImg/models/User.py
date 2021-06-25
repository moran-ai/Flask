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

