from flask import Flask, Blueprint, make_response, request
from order import order

from users import user_bp

app = Flask(__name__)
# 注册蓝图
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(order, url_prefix='/order')


@app.route('/')
def hello_world():
    response = make_response('Hello World!')
    # 默认cookie有效时间是浏览器关闭
    response.set_cookie('username', 'aaaa', max_age=1800)
    return response


@app.route('/get')
def get():
    resp = request.cookies.get('username')
    print(resp)
    return '获得cookie'


if __name__ == '__main__':
    app.run(debug=True)
