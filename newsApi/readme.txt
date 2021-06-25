跨域问题来源于JavaScript的"同源策略"，即只有 协议+主机名+端口号 (如存在)相同，
则允许相互访问。也就是说JavaScript只能访问和操作自己域下的资源，不能访问和操作其他域下的资源。
跨域问题是针对JS和ajax的，html本身没有跨域问题。
https://blog.csdn.net/itcats_cn/article/details/82318092

后端：
    1.使用第三方扩展：
        pip install flask-cors

    from flask_cors import CORS
    cors = CORS()

    与app进行绑定
    supports_credentials 添加证书保护
    cors.init_app(app=app, supports_credentials=True)

    2.make_response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-request-with, Content-type'

蓝图与api使用
user_bp = Blueprint('user', __name__)
api = Api(user_bp)

classXxxApi(Resource):
    pass

api.add_resource(classXxxApi, '/xxx')

使用缓存  redis 数据库
安装:
    pip install redis  安装redis依赖
    pip install flask-caching  安装缓存
