from flask import Blueprint
from flask import render_template
from flask import request
from apps.user.model import User
from flask import redirect
from flask import url_for

# user是蓝图的名字,__name__是导入的名字
# 定义一个蓝图对象
user_bp = Blueprint('user', __name__)

# 列表中保存用户对象
users = []

@user_bp.route('/', endpoint='show')
def user_center():
    """
    用户展示
    :return:
    """
    return render_template('user/show.html',users=users)

@user_bp.route('/register', methods=['GET', 'POST'])
def user_register():
    """
    用户注册
    :return:
    """
    if request.method == 'POST':
        # 获取提交的数据
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        # 验证密码唯一
        if password == repassword:
            # 验证用户名唯一
            for user in users:
                if user.username == username:
                    return render_template('user/register.html', msg='用户名已存在')
            # 创建用户对象
            user = User(username, password, phone)
            # 添加到用户列表
            users.append(user)
            # return redirect('/')
            # 注册成功后返回登录页面
            l = '注册成功'
            # return render_template('user/login.html', l=l)
            return redirect(url_for('user.show'))
            # return redirect('/login')
    return render_template('user/register.html')

@user_bp.route('/login', methods=['GET', 'POST'])
def user_login():
    """
    用户登录
    :return:
    """
    # 获取输入的用户名和密码
    username = request.form.get('username')
    password = request.form.get('password')
    for user in users:
        # 判断密码和用户名是否相同
        if user.username == username and user.password == password:
            return '<h1>登录成功</h1>'
    return '<h1>登录失败，检查用户名和密码是否正确</h1>'

@user_bp.route('/del')
def del_user():
    # 获取传递的username
    username = request.args.get('username')
    for user in users:
        if user.username == username:
            users.remove(user)
            # return redirect('/')
            return redirect(url_for('user.show'))
            # return '删除成功'
    else:
        return '删除失败'
    # return redirect(url_for('user.show'))

@user_bp.route('/update', methods=['GET', 'POST'])
def user_update():
    if request.method == 'POST':
        # 用户真实姓名
        relname = request.form.get('relname')
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        for user in users:
            if user.username == relname:
                user.username = username
                user.phone = phone
                return redirect(url_for('user.show'))
    else:
        username = request.args.get('username')
        for user in users:
            if user.username == username:
                return render_template('user/update.html', user=user)

@user_bp.route('/exit', methods=['GET', 'POST'])
def user_exit():
    return '用户退出'
