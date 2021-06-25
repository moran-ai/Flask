from flask import Flask

class DefaultConfig:
    USER = 'H'
    PWD = '12334'


server = Flask(__name__)
server.config.from_object(DefaultConfig)

@server.route('/')
def index():
    print(server.config['USER'])
    print(server.config['PWD'])
    return 'Hello Word'


if __name__ == '__main__':
    server.run(debug=True)
