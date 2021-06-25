"""
自定义的web框架
"""
import time
from functools import wraps

route_list = []


# 自定义个装饰器
def route(request_path):
    def add_route(func):
        # 添加路由到列表中
        route_list.append((request_path, func))

        @wraps(func)
        def invoke(*args, **kwargs):
            # 调用指定路由的函数
            return func()

        return invoke

    return add_route

def handle_request(params):
    request_path = params['request_path']
    for path, func in route_list:
        if request_path == path:
            return func()
    # # 如果请求的路径为index.html，则进行数据的返回
    # if request_path == '/index.html':
    #     return index()
    # elif request_path == '/user-info.html':
    #     return user_info()
    # 否则返回not found页面
    else:
        return page_not_found()

@route('/index.html')
def index():
    # 需求：打印当前系统时间
    data = time.strftime("%Y-%m-%d: %H-%M-%S", time.localtime())
    with open('template/index.html', 'r', encoding='utf-8') as f:
        response_content = f.read()
    # response_content = data
    response_content = response_content.replace('{%data%}', data)
    response_first_line = 'HTTP/1.1 200 OK\r\n'
    response_header = response_first_line + 'Server: MyServer\r\n'
    response = (response_header + '\r\n' + response_content).encode('utf-8')
    return response

@route('/user-info.html')
def user_info():
    data = time.strftime("%Y-%m-%d: %H-%M-%S", time.localtime())
    with open('template/user-info.html', 'r', encoding='utf-8') as f:
        response_content = f.read()
    response_content = response_content.replace('{%data%}', data)
    response_first_line = 'HTTP/1.1 200 OK\r\n'
    response_header = response_first_line + 'Server: MyServer\r\n'
    response = (response_header + '\r\n' + response_content).encode('utf-8')
    return response


def page_not_found():
    with open('static/404.html', 'rb') as f:
        response_content = f.read()  # 字节数据
    # 字符数据
    response_first_line = 'HTTP/1.1 404 Not Found\r\n'
    response_header = response_first_line + 'Server: MyServer\r\n'
    response = (response_header + '\r\n').encode('utf-8') + response_content
    return response


# route_list = {
#     ('/index.html', index),
#     ('/user-info.html', user_info)
# }


