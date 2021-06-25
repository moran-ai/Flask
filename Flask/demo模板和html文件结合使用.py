# html文件和模板结合使用
# jinjia2 模板引擎
from flask import Flask
from flask import request
from flask import render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)

@app.route('/register')
def register():
    # 通过模板引擎(Jinjia2)找到模板文件夹中的html文件,将html文件转为字符串形式
    r = render_template('index.html')  # 默认去模板文件夹(templates)中找文件
    print('---->',type(r))  # str
    return  r # 返回的是字符串类型

@app.route('/register1', methods=['get', 'post'])
def register1():
    print(request.full_path)  # /register1?username=7894566&address=asdddddd
    print(request.path) # /register1
    # 只能取出get请求数据
    print(request.args)  # ImmutableMultiDict([('username', '7894566'), ('address', 'asdddddd')])
    # get请求获取usernama和address
    print(request.args.get('username'))
    print(request.args.get('address'))

    # post请求数据获取
    print(request.form)
    print(request.form.get('username'))
    print(request.form.get('address'))
    return '注册成功'

if __name__ == '__main__':
    print(app.url_map)   # 打印路由规则表
    app.run()
