from flask import Flask, json

app = Flask(__name__, static_url_path='/h')


@app.route('/')
def hello_world():
    # rules:项目的所有的路由列表
    rules = app.url_map.iter_rules()
    # rule.endpoint视图函数  rule.rule：url地址
    return json.dumps({rule.endpoint: rule.rule for rule in rules})


@app.route('/user/<int(min=1):id>')  # 类型转换 flask 使用<>号
def user(id):
    print(type(id))
    return f'当前用户是：{id}'


if __name__ == '__main__':
    app.run(debug=True)
