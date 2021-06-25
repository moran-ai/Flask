from flask import Flask
from flask import render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)

@app.route('/base')
def load_base():
    """
    extends和block的使用
    :return:
    """
    return render_template('base.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    extends和block的使用
    :return:
    """
    return render_template('zi.html')

@app.route('/welcome')
def welcome():
    """
    include的使用
    :return:
    """
    return render_template('welcome.html')

@app.route('/macro')
def use_macro():
    """
    宏的使用
    调用宏
    :return:
    """
    return render_template('macro/macro1.html')

@app.route('/macro1')
def use_macro1():
    return render_template('macro/macro2.html')

if __name__ == '__main__':
    app.run()
