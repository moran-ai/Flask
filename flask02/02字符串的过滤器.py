from flask import Flask, render_template

app = Flask(__name__)

student = {
    'name': 'zhangsan',
    'age': 23,
    'gender': '男'
}

student_list = [
    {'name': 'lisi', 'age': 33, 'gender': '男'},
    {'name': 'limei', 'age': 23, 'gender': '女'},
    {'name': 'wangwu', 'age': 34, 'gender': '男'}
]

student_dict = {
    'a': {'name': 'lisi', 'age': 33, 'gender': '男'},
    'b': {'name': 'limei', 'age': 23, 'gender': '女'},
    'c': {'name': 'wangwu', 'age': 34, 'gender': '男'}
}


# 模板数据进行打开，传递一个字典 使用**
@app.route('/')
def hello_world():
    return render_template('04字符串的过滤器.html')


@app.route('/int')
def hello():
    return render_template('05数字的过滤器.html')


@app.route('/list')
def h_list():
    return render_template('06列表的过滤器.html')


@app.route('/dict')
def h_dict():
    return render_template('07字典的过滤器.html')


def get_top3(lit):
    """
    自定义模板模过滤器
    取出列表的前三个元素
    :param lit:
    :return:
    """
    return lit[:3]
# 第一种方式:注册一个过滤器
app.jinja_env.filters['get_top'] = get_top3

# 第二种方式
@app.template_filter('get_qu')
def get_qu(lit):
    """
    计算列表中每个元素的平方
    :param lit:
    :return:
    """
    return list(map(lambda x: x * x, lit))


@app.route('/test')
def test():
    return render_template('08自定义过滤器.html')

# # 模板传送一个列表
# @app.route('/t')
# def hello_world1():
#     return render_template('02.html', student_list=student_list)
#
#
# # 模板传送一个嵌套字典
# @app.route('/t1')
# def hello_world2():
#     return render_template('03.html', student_dict=student_dict)


if __name__ == '__main__':
    app.run(debug=True)
