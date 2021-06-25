"""
自定义一个web服务器
"""
import socket
import sys
import threading
import time
import MyFrameWork


class MyHttpWebServer:
    def __init__(self, port):
        # 创建套接字
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口复用,程序退出之后不需要等待几分钟，直接释放端口
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定IP地址
        server_socket.bind(('', port))
        # 设定监听的个数
        server_socket.listen(128)
        # 变为成员变量
        self.server_socket = server_socket

    # 处理请求的函数
    @staticmethod
    def handle_browser_request(new_socket):
        # 接收请求过来的数据
        recv_data = new_socket.recv(4096)
        if len(recv_data) == 0:
            # 关闭套接字
            new_socket.close()
            return
            # 对请求的数据进行解码
        request_data = recv_data.decode('utf-8')
        print('浏览器请求的数据为：', request_data)
        request_array = request_data.split(' ', maxsplit=2)
        request_path = request_array[1]
        print(f'请求路径是： {request_path}')

        # 如果请求路径为/，那么请求的路径默认为/index.html
        if request_path == '/':
            request_path = '/index.html'

        # 根据请求路径判断是静态资源还是动态资源
        if request_path.endswith('.html'):
            """ 动态资源的请求 """
            # 动态资源的处理交给web框架，需要传参数给web框架,可能会有多个参数，所以采用字典结构
            params = {
                'request_path': request_path
            }
            # 传参数给自定义的web框架
            response = MyFrameWork.handle_request(params=params)
            new_socket.send(response)   # 发送请求
            new_socket.close()
        else:
            """ 静态资源的请求 """
            response_header = None
            response_content = None
            response_first_line = None
            response_type = 'text/html'
            # 根据请求路径读取static目录中的静态文件的资源，响应给客户端
            try:
                # rb:兼容模式，可以读取图片，也可以读取js文件
                with open('static' + request_path, 'rb') as f:
                    response_content = f.read()
                if request_path.endswith('.jpg'):
                    response_type = 'image/webp'
                response_first_line = 'HTTP/1.1 200 OK\r\n'
                response_header = response_first_line + 'Server: MyServer\r\n'
            # 请求的文件不存在
            except Exception as e:
                with open('static/404.html', 'rb') as f:
                    response_content = f.read()  # 字节数据
                # 字符数据
                response_first_line = 'HTTP/1.1 404 Not Found\r\n'
                response_header = 'Server: MyServer\r\n'
            finally:
                response = (response_header + '\r\n').encode('utf-8') + response_content
                new_socket.send(response)  # 将响应的数据发送给浏览器

    # 启动服务器，接收客户端的请求
    def start(self):
        # 多线程循环接收
        while True:
            # 接收客户端的ip和端口
            new_socket, ip_port = self.server_socket.accept()
            print(f'客户端的ip地址是{ip_port}')
            # 将请求交给线程处理
            sub_thread = threading.Thread(target=self.handle_browser_request, args=(new_socket,))
            sub_thread.setDaemon(True)
            sub_thread.start()


def main():
    myweb = MyHttpWebServer(8080)
    myweb.start()


if __name__ == '__main__':
    main()
