from datetime import datetime
from exts import db

class BaseModel(db.Model):
    __abstract__ = True  # 指明是父类表，只用来继承
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_time = db.Column(db.DateTime, default=datetime.now)
