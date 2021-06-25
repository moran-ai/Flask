from flask import Flask
from flask import request
import settings
# print(__name__)  # __main__

"""
Flask源码分析：
    def __init__(
            self,
            import_name,
            static_url_path=None,
            static_folder="static",
            static_host=None,
            host_matching=False,
            subdomain_matching=False,
            template_folder="templates",
            instance_path=None,
            instance_relative_config=False,
            root_path=None,
        ):
"""

#  源码中name没有默认值，需要手动赋值
app = Flask(__name__)  # 实例一个Flask对象
app.config.from_object(settings)

# request对象
@app.route('/')  # 路由
def index():   # 视图函数
    print(request.headers)  # 打印请求头   request对象可以访问属性，也可以调用方法
    print(request.path)  # /
    print(request.full_path)  # /?
    print(request.base_url)
    print(request.url)
    return 'Hello World'

# 源码中的WSGI
# WSGI:Web服务器网关接口 Python Web Server Gateway Interface，缩写为WSGI
app.run()   # run()是Flask类中的一个方法，用来启动flask项目
