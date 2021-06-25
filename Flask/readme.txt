flask项目结构
--项目名
    ---static (静态)  js css
    ---templates (模板)
    ---app.py (运行|启动)

web项目:
    mvc:
        model 模型
        view  视图
        controler  控制器

python:
    mtv:
        model 模型
        template 模板 --> html
        view  视图  起控制作用  python 代码

b/s:
    browser 浏览器
    server 服务器

c/s:
    client: 客户端
    server: 服务器

 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

app = Flask(__name__)

app.run(host="ip地址", port='端口号')
ip地址，一个端口号对应一个程序
host设置为0.0.0.0 外网可以访问
默认只能是本机访问

debug:布尔类型
debug=True: 开启debug调试模式，只要代码改变就会自动重新加载新的代码  适用于开发环境(development)
debug=False: 默认 代码改变也不会自动去加载  适用于production环境

环境：
    1.production
    2.development
    3.testing

设置配置文件：
    # 修改flask项目配置文件
    ENV = 'development'
    DEBUG = True

    # 创建setting.py文件
    ENV = 'development'
    DEBUG = True

    将settings.py文件加入app.py
    第一种方式：
        import settings
        app.config.from_object(settings)

    第二种方式：
        app.config.from_pyfile('settings.py')

路由的请求和响应：
    1.浏览器地址栏输入的内容:http://0.0.0.0:8080/ ---> 服务器--->app.py文件--->有没有这个路由--->
    执行路由匹配的函数 ---> return 'Hello World' ---> response ---> 客户端的浏览器

    2.请求：request
            http协议:
            request:请求
            response:响应

    请求行：请求的地址和方法
    请求头：key:value
    请求体：get 没有请求体 post 有请求体

    响应行: 状态码
        200:请求成功
        302:重定向
        404:请求无法完成
        505:内部服务器错误 代码有问题

    响应头:key:value
    响应体:想要用户看到什么内容

flask中文文档  https://dormousehole.readthedocs.io/en/latest/
