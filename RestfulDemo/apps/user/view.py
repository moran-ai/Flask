import os

from flask import Blueprint, url_for
from flask_restful import Resource, marshal_with, fields, reqparse, inputs, marshal
from werkzeug.datastructures import FileStorage

from apps.user.model import User, Friend
from exts import api, db
from settings import Config

user_bp = Blueprint('user', __name__, url_prefix='/api')

class Isdelete(fields.Raw):
    def format(self, value):
        # print('--------->', value)
        return '删除' if value else '未删除'

user_fields_1 = {
    'id': fields.Integer,
    'username': fields.String,
    'uri': fields.Url('single_user', absolute=True)
    # 'password': fields.String,
    # 'phone': fields.String,
    # 'icon': fields.String,
    # 'isDelete': fields.Boolean(attribute='isdelete'),
    # 'isDelete1': Isdelete(attribute='isdelete'),
    # 'udatetime': fields.DateTime(dt_format='rfc822')
}

# 格式化文件的格式
user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'phone': fields.String,
    'icon': fields.String,
    'isDelete': fields.Boolean(attribute='isdelete'),
    'isDelete1': Isdelete(attribute='isdelete'),
    'udatetime': fields.DateTime(dt_format='rfc822')
}

# 参数解析
parser = reqparse.RequestParser(bundle_errors=True)  # 返回一个解析对象

# 再次验证前端输入的数据
# location=['form']  限制必须是一个POST请求
'''
location=['form', 'args', 'headers', 'cookies', 'files']
form: POST请求
args: GET请求
headers: 请求头
cookies: cookie
files: 文件上传     type=werkzeug.datastructures.FileStorage
'''
# 进
parser.add_argument('username', type=str, required=True, help='必须输入用户名', location=['form'])
parser.add_argument('password', type=inputs.regex(r'^\d{6,12}$'), required=True, help="必须输入6~12位的纯数字密码", location=['form'])
parser.add_argument('phone', type=inputs.regex(r'^1[3456789]\d{9}$'), location=['form'], help='手机号码格式错误')
parser.add_argument('hobby', action='append')
parser.add_argument('icon', type=FileStorage, location=['files'])

# 定义类视图
class UserResource(Resource):
    # get请求的处理
    @marshal_with(user_fields_1)
    def get(self):
        users = User.query.all()
        # return {'number': len(users), 'userlist': users}
        return users  # 返回一个用户列表

    # post
    @marshal_with(user_fields)
    def post(self):
        # 解析参数
        # 获取前端提交的数据
        args = parser.parse_args()  # 经过验证
        username = args.get('username')
        password = args.get('password')
        phone = args.get('phone')
        hobby = args.get('hobby')
        icon = args.get('icon')
        # print('----->', hobby)
        print('用户头像是------->', icon)
        user = User()
        # 存入数据库
        user.username = username
        user.password = password
        if icon:
            save_path = os.path.join(Config.UPLOAD_DIR, icon.filename)
            icon.save(save_path)
            user.icon = os.path.join('upload/icon', icon.filename)
        if phone:
            user.phone = phone
        db.session.add(user)
        db.session.commit()
        return user

    # put
    def put(self):
        return {'msg': '-------->put'}

    # delete
    def delete(self):
        return {'msg': '-------->delete'}

class UserSimpleResource(Resource):
    @marshal_with(user_fields)  # user转为一个序列化对象
    def get(self, id):
        user = User.query.get(id)
        return user  # 不是str, string, list...

    def put(self, id):
        print('endpoint的使用', url_for('all_user'))
        return {'msg': 'ok'}

    def delete(self, id):
        pass

user_friends_fields = {
    'username': fields.String,
    'nums': fields.Integer,
    'friends': fields.List(fields.Nested(user_fields))
}

class UserFriendResource(Resource):
    @marshal_with(user_friends_fields)
    def get(self, id):
        # 取出用户的朋友
        friends = Friend.query.filter(Friend.uid==id).all()
        # 取出该用户
        user = User.query.get(id)

        # 列表
        friend_list = []
        for friend in friends:
            u = User.query.get(friend.fid)
            friend_list.append(u)

        # 方法一：使用marshal()方法
        # data = {
        #     'username': user.username,
        #     'nums': len(friends),
        #     'friends': marshal(friend_list, user_fields)
        # }

        # 方法二：使用marshal_with()
        data = {
            'username': user.username,
            'nums': len(friends),
            'friends': friend_list
        }
        return data

# 获取所有用户信息
api.add_resource(UserResource, '/user', endpoint='all_user')
# 获取单个用户信息路由
api.add_resource(UserSimpleResource, '/user/<int:id>', endpoint='single_user')
api.add_resource(UserFriendResource, '/friend/<int:id>', endpoint='user_friend')

