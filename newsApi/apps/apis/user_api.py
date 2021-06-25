import random

from flask import Blueprint, session
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal
from werkzeug.security import generate_password_hash, check_password_hash

from apps.models.user_model import User
from exts import cache, db

user_bp = Blueprint('user', __name__)
api = Api(user_bp)

# 发送验证码输入
sms_parser = reqparse.RequestParser()
sms_parser.add_argument('mobile', type=inputs.regex(r'^1[35789]\d{9}$'),
                        help='手机号码格式错误', required=True, location=['form', 'args'])

# 发验证码
'''
class SendMessageApi(Resource):
    def post(self):
        args = sms_parser.parse_args()
        mobile = args.get('mobile')
'''

# 登录注册输入
lr_parser = sms_parser.copy()
# required=True 必填项
lr_parser.add_argument('code', type=inputs.regex(r'^\d{4}$'), help='验证码错误', required=True, location='form')

# 登陆注册输出
user_fields = {
    'id': fields.Integer,
    'username': fields.String
}

# 登录注册
class LoginAndRegisterApi(Resource):
    def post(self):
        # 取出post请求的数据
        args = lr_parser.parse_args()
        mobile = args.get('mobile')  # 手机号码
        code = args.get('code')  # 输入的验证码
        cache_code = cache.get(mobile)  # redis中的验证码
        if cache_code and code == cache_code:
            # 数据库中查找是否存在mobile(手机号)
            user = User.query.filter(User.phone == mobile).first()
            # 判断列表是否存在用户
            if not user:
                # 注册
                user = User()
                user.phone = mobile
                # 随机产生用户名，用户名为0, 9之间的13位数
                s = ''
                for i in range(13):
                    ran = random.randint(0, 9)
                    s += str(ran)
                user.username = '用户' + s
                db.session.add(user)
                db.session.commit()
            # 登录处理  记录登录状态: session, cookie, cache(redis)
            cache.set(mobile + '_', 1)
            return marshal(user, user_fields)  # 定制输出,两种方式：(1) marshal()  (2) @marshal_with
        else:
            return {'errmsg': '验证码错误', 'status': 400}

# 忘记密码
class ForgetPasswordApi(Resource):
    def get(self):
        s = 'q5we77rerQFSS5MS55AJ55DFA9043fsd343faDASrfasf44F4311AS324FA54a4sdfA54SDas123'
        code = ''
        # 随机生成四位数验证码
        for i in range(4):
            ran = random.choice(s)
            code += ran
        # 保存验证码
        session['code'] = code
        # 返回验证码
        return {'code': code}

# 重置密码输入
reset_parser = sms_parser.copy()
reset_parser.add_argument('image_code', type=inputs.regex(r'^[a-zA-Z0-9]{4}$'), help='输入正确格式的验证码')

# 重置密码
class ResetPasswordApi(Resource):
    def get(self):
        # 获取信息
        args = reset_parser.parse_args()
        # 页面中输入的手机号
        mobile = args.get('mobile')
        # 图形验证码
        imageCode = args.get('image_code')
        # 输入的验证码
        code = session.get('code')
        # 如果验证码一致
        if code and imageCode.lower() == code.lower():
            # 通过手机号判断用户是否存在
            user = User.query.filter(User.phone == mobile).first()
            if user:
                # 信息发送验证码
                '''
                    ret, smscod = send_duanxina(mobile)
                    if ret is not None:
                        if ret['code'] == 200:
                            cache.set(mobile, smscod, timeout=1800)
                            return jsonify(code=200, msg='短信发送成功')
                    else:
                        print('ERROR: ret.code=%s, msg=%s' % (ret['code'], ret['msg'])
                        return jsonify(code=400, msg='短信发送失败')
                '''
            else:
                return {'status': 400, 'msg': '此用户未注册'}
        else:
            return {'status': 400, 'msg': '验证码错误或超时'}

# 更新密码
# 客户端需要传入的信息
# update_parser = reqparse.RequestParser()
update_parser = lr_parser.copy()
# 验证码
update_parser.add_argument('code', type=inputs.regex(r'^\d{4}$'), location='from', help='输入验证码')
# 密码
update_parser.add_argument('password', type=inputs.regex(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{8,10}$'),
                           help='必须包含大小写字母和数字的组合，不能使用特殊字符，长度在 8-10 之间', location='form')
# 确认密码
update_parser.add_argument('repassword', type=inputs.regex(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{8,10}$'),
                           help='必须包含大小写字母和数字的组合，不能使用特殊字符，长度在 8-10 之间', location='form')

'''
# 更新密码
class UpdatePasswordApi(Resource):
    def post(self):
        # 获取信息
        args = update_parser.parse_args()
        # 获取验证码
        code = args.get('code')
        # 手机号
        mobile = args.get('mobile')
        # 缓存中的验证码
        cache_code = cache.get(mobile)
        # 如果缓存中的验证码等于输入的验证码  将对应用户的密码进行更新
        if cache_code and cache_code == code:
            # 通过手机号找到对应的用户
            user = User.query.filter(User.phone == mobile).first()
            password = args.get('password')
            repassword = args.get('repassword')
            # 如果两次密码一致
            if repassword == password:
                # 密码加密
                user.password = generate_password_hash(password)
                db.session.commit()
                return {'status': 200, 'msg': '设置密码成功'}
            else:
                return {'status': 400, 'msg': '两次密码不一致'}
        else:
            return {'status': 400, 'msg': '验证码错误'}
'''
# 登录设置需要前端传入的内容
# 账号密码登录
password_login_parser = sms_parser.copy()
password_login_parser.add_argument('password', type=str, help='必须输入密码', required=True, location='form')

class UserApi(Resource):
    def post(self):
        """
        用户账号密码登录
        :return:
        """
        args = password_login_parser.parse_args()
        # 手机号
        mobile = args.get('mobile')
        # 密码
        password = args.get('password')
        # 判断用户是否存在
        user = User.query.filter(User.phone == mobile).first()
        if user:
            # 判断用户密码是否一致
            if check_password_hash(user.password, password):
                # 登录成功后记录用户信息
                cache.set(mobile + '_', 1)
                return {'status': 200, 'msg': '用户登录成功'}
        return {'status': 400, 'msg': '账号或密码错误'}

    def put(self):
        """
        用户密码修改
        :return:
        """
        # 获取信息
        args = update_parser.parse_args()
        # 获取验证码
        code = args.get('code')
        # 手机号
        mobile = args.get('mobile')
        # 缓存中的验证码
        cache_code = cache.get(mobile)
        # 如果缓存中的验证码等于输入的验证码  将对应用户的密码进行更新
        if cache_code and cache_code == code:
            # 通过手机号找到对应的用户
            user = User.query.filter(User.phone == mobile).first()
            password = args.get('password')
            repassword = args.get('repassword')
            # 如果两次密码一致
            if repassword == password:
                # 密码加密
                user.password = generate_password_hash(password)
                db.session.commit()
                return {'status': 200, 'msg': '设置密码成功'}
            else:
                return {'status': 400, 'msg': '两次密码不一致'}
        else:
            return {'status': 400, 'msg': '验证码错误'}

api.add_resource(LoginAndRegisterApi, '/codelogin')
api.add_resource(ForgetPasswordApi, '/forgetpd')
api.add_resource(ResetPasswordApi, '/resetpd')
api.add_resource(UserApi, '/user')
# api.add_resource(PasswordLogin, '/pwdlogin')
