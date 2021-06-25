from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'msbtest'
USERNAME = 'root'
PASSWORD = 'itcast'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 创建数据表
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(40))
    password = db.Column(db.String(255))

    def __repr__(self):
        return f'用户编号：{self.id} ---> 用户名：{self.uname} ---> 密码: {self.password}'


# db.create_all()  # 创建数据表user
# db.drop_all()
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/add')
def add_data():
    name = request.args.get('name')
    pwd = request.args.get('password')
    user = User()
    user.uname = name
    user.password = pwd
    db.session.add(user)
    db.session.commit()
    return '数据添加成功'


@app.route('/query')
def query():
    id = request.args.get('id')
    user = db.session.query(User).filter(User.id == id).first()
    return f'查到的用户是：{user}'


@app.route('/delete')
def delete():
    id = request.args.get('id')
    user = User.query.filter(User.id == id).first()
    db.session.delete(user)
    db.session.commit()
    return f'用户{user.uname}删除成功'

@app.route('/update')
def update():
    id = request.args.get('id')
    user = User.query.filter(User.id == id).first()
    user.uname = '赵六'
    user.password = '123456'
    db.session.add(user)
    db.session.commit()
    return '数据修改成功'

if __name__ == '__main__':
    app.run(debug=True)
