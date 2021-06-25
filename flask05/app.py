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
