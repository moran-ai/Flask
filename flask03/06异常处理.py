from flask import Flask, Blueprint, abort, request, render_template
from order import order

from users import user_bp

app = Flask(__name__)


# 注册蓝图


@app.route('/')
def hello_world():
    100 / 0
    name = request.args.get('name')
    if name:
        print(name)
    else:
        abort(500)
    return 'Hello World!'


# 捕获不存在页面
@app.errorhandler(404)
def test(error):
    print(error)
    return render_template('404.html'), 404


# 捕获指定的错误
@app.errorhandler(ZeroDivisionError)
def test12(error):
    print(error)
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
