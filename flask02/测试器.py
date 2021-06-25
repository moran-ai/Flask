import re
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/test_demo')
def test():
    return render_template('09测试器.html')


# 自定义测试器
def test_phone(phone):
    phone_re = '1[3-9]\d{9}'
    return re.match(phone_re, phone)

app.jinja_env.tests['phone_test'] = test_phone

# 两种注册测试器的方法
# ① 使用app.jinja_env.tests的方法
# ② 使用@app.template_test()的方法

if __name__ == '__main__':
    app.run(debug=True)
