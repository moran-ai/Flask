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
    'a':{'name': 'lisi', 'age': 33, 'gender': '男'},
    'b':{'name': 'limei', 'age': 23, 'gender': '女'},
    'c': {'name': 'wangwu', 'age': 34, 'gender': '男'}
}


# 模板数据进行打开，传递一个字典 使用**
@app.route('/')
def hello_world():
    return render_template('01.html', **student)


# 模板传送一个列表
@app.route('/t')
def hello_world1():
    return render_template('02.html', student_list=student_list)


# 模板传送一个嵌套字典
@app.route('/t1')
def hello_world2():
    return render_template('03.html', student_dict=student_dict)


if __name__ == '__main__':
    app.run(debug=True)
