from flask import Flask
from flask import render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)

@app.route('/')
def hello_world():
    msg = 'hello world and hello everyone'
    li = [2, 3, 4, 5, 6]
    return render_template('show3.html', msg=msg, li=li)

# 第一种方式实现自定义过滤器，使用add_template_filter(自定义函数名, '自定义过滤器名')函数
def repalce_hello(value):
    """
    过滤器本质上是一个函数
    自定义过滤器
    替换hello
    :param value:
    :return:
    """
    print('------>', value)
    value = value.replace('hello', '')
    print('======>', value)
    return value.strip()

# 自定义模板过滤器
app.add_template_filter(repalce_hello, 'replace')

# 第二种方式实现过滤器，使用装饰器
@app.template_filter('listreverse')
def reverse_list(li):
    temp_li = list(li)
    temp_li.reverse()
    return temp_li

if __name__ == '__main__':
    app.run()
