import hashlib

from flask import Blueprint, request, render_template, redirect, url_for
from sqlalchemy import or_, and_, not_

from apps.user.model import User
from exts import db

# 创建蓝图对象
user_bp = Blueprint('user', __name__)

# 用户注册
@user_bp.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 获得post请求的数据
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        # 查询数据库中的信息
        users = User.query.all()
        # 验证用户名是否唯一
        for user in users:
            if user.username == username:
                return '<h1 style="color:red; font-size=20px">用户名已被使用，请重新输入</h1>'
            if password != repassword:
                return '<h1 style="color:red; font-size=20px">两次密码不一致，请重新输入密码</h1>'
        # 验证两次密码输入是否一致
        if password == repassword:
            # 与模型结合
            # 1.创建一个模型对象
            user = User()
            # 2.给对象赋值
            user.username = username
            # 使用hashlib中的sha256对密码进行加密
            user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            user.phone = phone
            # 将数据添加到数据库
            # 3.将User对象添加到session中(类似缓存)
            db.session.add(user)
            # 4.提交数据到数据库
            db.session.commit()
            # 注册成功后返回用户中心，展示注册的用户
            return redirect(url_for('user.user_center'))
        # else:
        #     return redirect(url_for('user.user_center'))
            # return render_template('user/register.html', msg='两次密码不一致')
    return render_template('user/register.html')

# 用户中心
@user_bp.route('/center')
def user_center():
    # 查询数据库中的信息
    users = User.query.filter(User.isdelete==False).all() # select * from user; 返回列表

    return render_template('user/center.html', users = users)

# 用户登录
@user_bp.route('/login', methods = ['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 对密码进行加密
        new_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # 查询 select * from user where username='xxx';
        user_list = User.query.filter_by(username=username)
        # user_list = User.query.filter_by(username=username).first()取出满足条件的第一条数据
        for u in user_list:
            if u.password == new_password:
                return '登录成功'
        else:
            return render_template('user/login.html', msg='用户名或密码错误！')
    return render_template('user/login.html')

# 用户查询
@user_bp.route('/select')
def user_select():
    # 根据主键查询用户
    user = User.query.get(1)  # get(主键值) 返回一个用户对象
    # user1 = User.query.filter(User.username == 'wangwu').all()
    # user_list = User.query.filter(User.username.startswith('z')).all()  # 查询以z开头的所有数据
    # user_list = User.query.filter(User.username.contains('z')).all()  # 查询包含z的所有数据
    # user_list = User.query.filter(User.username.endswith('z')).all()  # 查询以z结尾的所有数据
    # or查询
    # user_list = User.query.filter(or_(User.username.like('z%'), User.username.contains('i'))).all()

    # and查询  < 等效于__lt__   > 等效于__gt__
    # user_list = User.query.filter(and_(User.username.contains('i'), User.rdatetime < '2020-10-05 13:58')).all()

    # not查询
    # user_list = User.query.filter(not_(User.username.contains('i'))).all()

    # user_list = User.query.filter(User.phone.in_(['12345678123', '12345678124'])).all()
    # 排序 默认升序排列
    # user_list = User.query.filter(User.username.contains('z')).order_by(-User.rdatetime).all()
    # user_list = User.query.order_by('id').all()
    # user_list =

    # limit的使用+offset
    # user_list = User.query.order_by('id').limit(2).all()  取出前两行数据
    user_list = User.query.offset(2).limit(2).all()  # offset(2)跳过两个数据，在取数据
    return render_template('user/select.html', user=user, user1=user_list)

# 用户搜索
@user_bp.route('/search')
def search():
    keyword = request.args.get('search')  # 用户名 | 手机号码
    # 查询
    user_list = User.query.filter(or_(User.username.contains(keyword), User.phone.contains(keyword))).all()
    return render_template('user/center.html', users=user_list)

# 用户删除
@user_bp.route('/delete')
def delete():
    """
    用户删除
    :return:
    """
    # 获取用户id
    user_id = request.args.get('id')
    # 1.逻辑删除 （更新）
    # # 获取id的用户
    # user = User.query.get(user_id)
    # # 逻辑删除 不是真正的删除，只是不显示
    # user.isdelete = True
    # # 提交
    # db.session.commit()

    # 2.物理删除
    user = User.query.get(user_id)
    # 将对象放在缓存中，准备删除
    db.session.delete(user)
    # 提交删除
    db.session.commit()

    return redirect(url_for('user.user_center'))

# 用户更新
@user_bp.route('/update', methods=['GET', 'POST'])
def user_update():
    """
    用户更新
    :return:
    """
    # 对展示在页面上的用户进行更新操作
    if request.method == 'POST':
        username = request.form.get('username')
        phone = request.form.get('phone')
        user_id = request.form.get('id')

        # 找用户
        user = User.query.get(user_id)

        # 修改用户信息
        user.username = username
        user.phone = phone

        #提交
        db.session.commit()
        return redirect(url_for('user.user_center'))
    else:
        # 获取要更新的用户，并展示在页面上
        user_id = request.args.get('id')
        user = User.query.get(user_id)
        return render_template('user/update.html', user=user)
