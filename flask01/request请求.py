from flask import Flask, request, jsonify, make_response, render_template

app = Flask(__name__, static_url_path='/h')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test1', methods=['GET'])
def test1():
    user_id = request.args.get('user_id')
    print(f'用户id是：{user_id}')
    name = request.args.get('name')
    print(f'用户是：{name}')
    return 'ok'


@app.route('/test2', methods=['GET', 'POST'])
def test2():
    if request.method == 'POST':
        name = request.form.get('user_name')
        age = request.form.get('user_age')
        print(name, age)
        print(f'类型是：{type(name), type(age)}')
        f = request.files['file']
        f.save('./static/demo.jpg')
        return 'okk'
    return None


# 返回一个json数据
@app.route('/demo')
def demo():
    json_data = {
        'name': 'zhangsan',
        'age': 320
    }
    return jsonify(json_data)


# 自定义响应  使用元组的方式
@app.route('/demo1')
def demo1():  # 响应有三部分：response, status, headers
    return '自定义响应的内容', 200, {'margin': 'python'}


# 自定义响应2 使用make_response函数
@app.route('/demo2')
def demo2():
    resp = make_response('make_response响应的内容')
    resp.status = '404 status'  # 响应状态
    resp.headers['my_param'] = 'python'
    return resp


@app.route('/demo3')
def demo3():
    return render_template('index.html', name='zhangsna', age=20)


if __name__ == '__main__':
    app.run(debug=True)
