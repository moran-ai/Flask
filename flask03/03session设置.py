import os
from flask import Flask, Blueprint, make_response, request, session
from order import order
from flask.json import JSONEncoder
from datetime import timedelta
from users import user_bp

app = Flask(__name__)
# 注册蓝图
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(order, url_prefix='/order')


class DefaultConfig():
    SECRET_KEY = os.urandom(24)
    # 设置会话的有效时间为30分钟
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)


app.config.from_object(DefaultConfig)


class My_JSONEncoder(JSONEncoder):
    """
    定义一个处理对象的类
    """

    def default(self, obj):
        """
        重写方法，自定义处理自定义类的方法
        :param o:
        :return:
        """
        if isinstance(obj, Person):
            return {
                'name': obj.name,
                'age': obj.age
            }


# 加入app配置中
app.json_encoder = My_JSONEncoder


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


@app.route('/')
def hello_world():
    print(app.config.get('SECRET_KEY'))
    session.permanent = True
    session['username'] = 'python'
    session['uid'] = '13354354'
    session['Person'] = Person  # 可以传递一个自定义的对象  需要进行序列化
    return 'ok'


@app.route('/get')
def get():
    usename = session.get('username')
    uid = session.get('uid')
    person = session.get('Person')
    print(usename, uid, person)
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)
