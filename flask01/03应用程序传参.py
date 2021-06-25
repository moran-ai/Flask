from flask import Flask

server = Flask(__name__)
server.config.from_pyfile('setting.py')
# server.config.from_envvar('系统环境中设定的名字',silent=True) # 从环境变量中进行加载  silent=True 安静模式


@server.route('/')
def index():
    print(server.config['USER'])
    print(server.config['PWD'])
    return 'Hello Word'


if __name__ == '__main__':
    server.run(debug=True)
