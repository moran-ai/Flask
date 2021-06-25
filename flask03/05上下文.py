import os
from flask import Flask, Blueprint, make_response, request, session, render_template, current_app
from order import order
from flask.json import JSONEncoder
from datetime import timedelta
from users import user_bp
from item import item_bp

app = Flask(__name__)
# 注册蓝图
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(order, url_prefix='/order')
app.register_blueprint(item_bp)


app.h = 'hello h'

@app.route('/')
def hello():
    return 'hello word'

# 捕获服务器500错误
@app.errorhandler(500)
def server_error(error):
    print(error)
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
