from flask import Flask
from flask import Response
from flask import make_response
import settings

app = Flask(__name__)
app.config.from_object(settings)
# print(app.config)  # 返回一个字典
# 修改配置文件中的环境  'ENV': 'production'
# app.config['ENV'] = 'development'  # 将原来的production(生产者)环境改为development(开发者)环境
# app.config['DEBUG'] = True  # 适用于开发者环境

@app.route('/')
def index():
    return '<h1>好的</h1>'
# return 后面返回的字符串做了response对象的封装，最终的返回结果还是response对象

# 返回Response()实例化对象
@app.route('/index')
def index1():
    response =  Response('<h1>Hello World</h1>')
    print(response.content_type)
    print(response.headers)
    print(response.status_code)  # 状态码
    print(response.status)  # 状态

    # 设置cookie
    response.set_cookie('name', 'abc')
    return response

# 返回字典
# data = {'a': '北京', 'b': '上海', 'c': '深圳'}
@app.route('/index1')
def index2():
    return {'a': '北京', 'b': '上海', 'c': '深圳'}

# 返回元组
# 返回的元组形式：'字符串', 状态码
@app.route('/index2')
def get_fun():
    return '北京', 200  # 元组

@app.route('/index3')
def index3():
    content = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>首页</title>
    <style>
        div{
             width: 100%;
            height: 100px;
            border: 2px solid red;
        }
    </style>
</head>
<body>
<h1>欢迎来到首页</h1>
<div>
    <ul>
        <li>hello</li>
        <li>abc</li>
        <li>wolrd</li>
    </ul>
</div>
</body>
</html>
    """
    respone = make_response(content)  # make_response()函数的返回值是一个response对象
    # 定制响应头
    respone.headers['mytest'] = '123abc'

    # 将定制好的response返回
    return respone

if __name__ == "__main__":
    app.run()
