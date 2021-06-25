from flask import Flask, Blueprint
from order import order

from users import user_bp

app = Flask(__name__)
# 注册蓝图
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(order, url_prefix='/order')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
