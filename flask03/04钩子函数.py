import os
from flask import Flask, Blueprint, make_response, request, session, render_template
from order import order
from flask.json import JSONEncoder
from datetime import timedelta
from users import user_bp

app = Flask(__name__)
# 注册蓝图
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(order, url_prefix='/order')


@app.before_first_request
def before_first_request():
    print('第一次请求执行,仅仅执行一次')


@app.before_request
def before_request():
    print('请求前进行执行,如果有返回值，下面的钩子函数和视图不会进行执行')


@app.after_request
def after_request(resp):
    print('请求后进行执行，有返回值')

    return resp


@app.teardown_request
def teardown_request(resp):
    print('请求结束时进行执行，有返回值')


@app.route('/')
def hello_word():
    resp = make_response('hh')
    return resp


@app.route('/g')
def h():
    return 'ol'


# 捕获服务器500错误
@app.errorhandler(500)
def server_error(error):
    print(error)
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
