import logging

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'qwe123rty'

logger = logging.getLogger('flask.app')
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log2.txt")
handler.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.route('/')
def index():
    logger.warning('首页的警告')
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 验证用户名是否匹配
        username = request.form.get('username')
        if username == 'admin':
            flash('登陆成功', 'info')  # flash有三种消息类型 : info, error, warning
            flash('enene', 'error')
            flash('呵呵', 'warning')
            # return render_template('index.html')
            return redirect(url_for('index'))
        else:
            # 添加日志
            # app.logger.debug('这是一个debug测试')
            # app.logger.error('这是一个error测试')
            # 需要指定logger的名字为app才可执行 logger = logging.getLogger('app')
            app.logger.warning('这是一个warning测试')
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
