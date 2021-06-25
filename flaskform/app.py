import os
from io import BytesIO

from flask import Flask, render_template, make_response, session
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
from werkzeug.utils import secure_filename

from form import UserForm
from util import generate_image

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwerty123'  # 设置令牌，不设置会报错
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
# 验证码处理
app.config['RECAPTCHA_PUBLIC_KEY'] = 'rtadfadffd44334545'  # 公钥
app.config['RECAPTCHA_PRIVATE_KEY'] = 'aeqrerfsdf1234678' # 私钥
# 可选
app.config['RECAPTCHA_PARAMETERS '] = {'hl': 'zh', 'render': 'explicit'}
app.config['RECAPTCHA_DATA_ATTRS '] = {'theme': 'dark'}

# csrf保护
csrf = CSRFProtect(app=app)
# 关联app
bootstrap = Bootstrap(app=app)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    uform = UserForm()  # 表单类对象
    if uform.validate_on_submit():
        # print(uform.name)
        # print(uform.password)
        name = uform.name.data
        password = uform.password.data
        phone = uform.phone.data
        icon = uform.icon.data
        filename = secure_filename(icon.filename)
        print('上传的文件名是：------------->', filename)
        print(name, password, phone)
        print(type(icon))  # <class 'werkzeug.datastructures.FileStorage'>

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        STATIC_DIR = os.path.join(BASE_DIR, 'static')
        UPLOAD_DIR = os.path.join(STATIC_DIR, 'upload')
        icon.save(os.path.join(UPLOAD_DIR, filename))
        return '提交成功'
    return render_template('user.html', uform=uform)

@app.route('/image')
def get_image():
    """
    返回值为图片
    :return:
    """
    img, code = generate_image(6)

    # 将图片转为二进制
    buffer = BytesIO()  # 创建一个二进制容器
    # 将图片存入二进制容器中
    img.save(buffer, 'JPEG')
    buf_bytes = buffer.getvalue()   # 获取容器中的值
    # 保存验证码到session中
    session['vailcode'] = code
    # 使用后make_response()构建response对象
    response = make_response(buf_bytes)

    # 设置请求头的类型
    response.headers['Content-Type'] = 'image/jpg'
    return response

# form与bootstrap结合
@app.route('/user', methods=['GET', 'POST'])
def boot_form():
    uform = UserForm()
    return render_template('user1.html', uform=uform)

if __name__ == '__main__':
    app.run()
