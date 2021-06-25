from flask import Flask, Blueprint
from flask_restful import Resource, Api, reqparse, inputs

app = Flask(__name__)
user_bp = Blueprint('user', __name__)
# 对外提供一个接口。可以访问某个资源
api = Api(app)


# 定义一个资源
class HelloResource(Resource):
    def get(self):
        return {'get': '获取资源'}

    def post(self):
        # ① 创建请求参数校验的对象
        rq = reqparse.RequestParser()
        # ② 定义参数的定义声明  required=True必填项
        rq.add_argument('a', required=True, help='参数a错误', type=int)  # 如果定义了help，所有的错误提示都会是同一个提示
        # action='append' 获取多个同名变量的值  默认获取第一个同名变量的值
        rq.add_argument('b', required=True, type=str, action='append')  # 如果定义了help，所有的错误提示都会是同一个提示
        # choices 参数规定的范围  参数只能选择choices里面的值
        rq.add_argument('c', required=True, type=str, choices=['男', '女'])  # 如果定义了help，所有的错误提示都会是同一个提示
        # 只允许两位数的整数，使用正则表达式
        rq.add_argument('d', required=True, type=inputs.regex('^\d{2}$'))  # 如果定义了help，所有的错误提示都会是同一个提示
        # 确定范围，只允许1到100的整数，包括1和100
        rq.add_argument('e', required=True, type=inputs.int_range(1, 100))  # 如果定义了help，所有的错误提示都会是同一个提示
        # 只允许传递boolean值  location：提交的位置  form为表单提交
        rq.add_argument('f', required=True, type=inputs.boolean, location='form')  # 如果定义了help，所有的错误提示都会是同一个提示
        # ③ 进行参数的校验
        req = rq.parse_args()
        # ④ 校验完成之后得到校验的值
        a = req.a
        b = req.b
        c = req.c
        d = req.d
        e = req.e
        f = req.f
        return {'post': '新建或者更新资源', 'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f}

    def put(self):
        return {'put': '更新资源'}

    def delete(self):
        return {'delte': '删除资源'}


# 资源绑定api
api.add_resource(HelloResource, '/hello')
# app.register_blueprint(user_bp, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)
