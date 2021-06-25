from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
import json
import settings

users = []
app = Flask(__name__)

# 加入修改后的配置文件
app.config.from_object(settings)

@app.route('/', endpoint='shouye')  # endpoint为路由的别名
def shouye():
    return render_template('shouye.html')

@app.route('/add/<int:n1>/<int:n2>')
def index(n1, n2):
    if n1 >0 and n2 >0:
        r = n1 + n2
        return "结果是：" + str(r)
    return '输入的两个数必须大于0'

@app.route('/index1', methods=['GET', 'POST'])
def index1():
    """
    注册
    使用模板
    将get和post请求相结合
    :return:
    """
    # 获取get请求数据 request.args.get()
    print(request.method)
    if request.method == 'POST':
        # 用户名
        username = request.form.get('username')
        # 密码
        password = request.form.get('password')
        # 确认密码
        repassword = request.form.get('repassword')
        # 用户密码一致性验证
        if password == repassword:
            # 保存用户和密码
            user = {'username': username, 'password': password}
            # 将用户名和密码存储到列表中
            users.append(user)
            # return '注册成功！<a href="/">返回首页</a>'
            # 1.使用重定向跳转
            # return redirect('/') # 有两次响应：1.302状态码 + location 2.返回location请求地址内容

            # 2.使用url_for()实现跳转重定向
            return redirect(url_for('shouye'))
        else:
            return '两次密码不一致，请重新输入密码！'
    return render_template('index1.html')

@app.route('/show')
def show():
    """
    显示注册的用户
    :return:
    """
    j_str = json.dumps(users)
    return j_str  # json字符串

@app.route('/test')
def test():
    url = url_for('shouye')  # url_for 路径反向解析
    # print(url)  # 返回/
    return 'test'

if __name__ == '__main__':
    # print(app.url_map)  # app.url_map 路由规则
    app.run()
