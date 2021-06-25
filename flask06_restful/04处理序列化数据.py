from flask import Flask
from flask_restful import Resource, Api, marshal, marshal_with, fields
from flask import make_response, current_app
from flask_restful.utils import PY3
from json import dumps

app = Flask(__name__)
# 对外提供一个接口。可以访问某个资源
api = Api(app=app)


# 定义一个模型类
class User(object):
    def __init__(self, user_id, password, username):
        self.user_id = user_id
        self.password = password
        self.user_name = username


# 将模型类变为一个序列化数据，使用fields定义一个转换的格式
property_fields = {
    'user_name': fields.String,
    'password': fields.String
}


# 加上装饰器
@api.representation('application/json')
def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""
    # 自定义一些内容
    if not 'message' in data:
        data = {
            'message': 'OK',
            'data': data
        }
    settings = current_app.config.get('RESTFUL_JSON', {})

    # If we're in debug mode, and the indent is not set, we set it to a
    # reasonable value here.  Note that this won't override any existing value
    # that was set.  We also set the "sort_keys" value.
    if current_app.debug:
        settings.setdefault('indent', 4)
        settings.setdefault('sort_keys', not PY3)

    # always end the json dumps with a new line
    # see https://github.com/mitsuhiko/flask/pull/1262
    dumped = dumps(data, **settings) + "\n"

    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp


# 定义一个资源
class HelloResource(Resource):
    # 使用自定义的格式
    @marshal_with(property_fields)
    def get(self):
        u = User(1, '李梅', '123456')
        # return marshal(u, property_fields,envelope='data1')
        return u

    def post(self):
        return {'post': '新建或者更新资源'}

    def put(self):
        return {'put': '更新资源'}

    def delete(self):
        return {'delte': '删除资源'}


# 资源绑定api
api.add_resource(HelloResource, '/hello')

if __name__ == '__main__':
    app.run(debug=True)
