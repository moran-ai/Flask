from flask import Flask,url_for,redirect
from werkzeug.routing import BaseConverter

app = Flask(__name__, static_url_path='/h')


class MobileConverter(BaseConverter):
    """
    自定义的转换器，继承当前的BaseConverter的父类
    定义一个匹配手机号的正则表达式
    """
    # regex要和父类的名字一致
    regex = r'1[3-9]\d{9}'


@app.route('/')
def hello_world():
    # url_for 生成一个动态的url地址
    return redirect(url_for('phone', mon_number='13456789012'))


# 将自定义的转换器添加到转换器列表中
app.url_map.converters['phone'] = MobileConverter


@app.route('/phone/<phone:mon_number>')
def phone(mon_number):
    return f'当前手机号是：{mon_number}'


if __name__ == '__main__':
    app.run(debug=True)
