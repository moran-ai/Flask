from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
# 对外提供一个接口。可以访问某个资源
api = Api(app=app)


# 定义一个资源
class HelloResource(Resource):
    def get(self):
        return {'get': '获取资源'}

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
