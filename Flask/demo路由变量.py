from flask import Flask
import settings

app = Flask(__name__)

# 加载自定义的配置文件
app.config.from_object(settings)

# 定义路由
@app.route('/')
def index():
    return '<font color="red">Hello World</font>'

"""
路由变量可以传递string,int,float,path(类似string,可以包含斜杠),uuid(接受UUID字符串)
uuid是通用唯一识别码
"""

# 路由变量
# <key>为传递的变量, get_city(key)中的key为变量   返回字典中的值
data = {'a': '北京', 'b': '上海', 'c': '深圳'}
@app.route('/get-city/<key>')
# 字符串类型
def get_city(key):
    """
    key为string类型
    :param key: key就是一个变量名 默认是stirng类型
    :return:
    """
    return data.get(key)

# int类型
@app.route('/add/<int:num>')
def add(num):
    """
    加法
    :param num:
    :return:
    """
    result = num + 10
    return str(result)   # 返回值只能是string，dict,tuple,response对象,WSGI，不能是int

# float类型
@app.route('/add1/<float:num>')
def add1(num):
    print('num--->' , type(num))
    return str(num)

# path类型 类似于string类型
@app.route('/index/<path:p>')
def get_path(p):
    print('======>', type(p))  # string类型
    return p

# uuid类型
# uuid是通过计算得出，不是随意输入的字符串 使用python中的自带的uuid库中的uuid4()方法计算uuid的值
@app.route('/test/<uuid:uid>')
def test(uid):
    print('====>>>>>', type(uid))
    return '获取唯一的标识码'

if __name__ == '__main__':
    app.run()  # 启动之前改变端口号，如果不用默认端口号
