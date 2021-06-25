from apps.models import BaseModel
from exts import db

class NewsType(BaseModel):
    """
    新闻分类
    """
    __tablename__ = 'news_type'
    type_name = db.Column(db.String(100), nullable=False)

class News(BaseModel):
    """
    新闻
    """
    __tablename__ = 'news'
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    content = db.Column(db.Text, nullable=False)
    new_type_id = db.Column(db.Integer, db.ForeignKey('news_type.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='news')

    def __str__(self):
        return self.title

class Comment(BaseModel):
    """
    评论
    """
    __tablename__ = 'comment'
    content = db.Column(db.String(500), nullable=False)
    love_num = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'))
    # 评论回复
    replays = db.relationship('Replay', backref='comment')
    def __str__(self):
        return self.content

class Replay(BaseModel):
    """
    回复  针对某一条评论
    """
    __tablename__ = 'replay'
    content = db.Column(db.String(500), nullable=False)
    love_num = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    def __str__(self):
        return self.content