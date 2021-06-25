from apps.models import BaseModel
from exts import db


class User(BaseModel):
    __tablename__ = 'user'
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200))
    phone = db.Column(db.String(11), unique=True, nullable=False)
    icon = db.Column(db.String(300))
    # 新闻列表
    newsList = db.relationship('News', backref='author')
    commetns = db.relationship('Comment', backref='user')
    # 回复
    replays = db.relationship('Replay', backref='user')
    def __str__(self):
        return self.username
