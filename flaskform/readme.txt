flask-wtform文档地址：
    http://www.pythondoc.com/flask-wtf/
    https://wtforms.readthedocs.io/en/2.3.x/

安装：
    pip install Flask-WTF

wtform:
    flask-wtf: 集成了wtform, csrf的保护和文件上传功能，图形验证码

全局使用csrf保护
csrf = CSRFProtect(app=app)
必须设置SECRET_KEY这个配置项
app.config['SECRET_KEY'] = 'XXXX'

各种Field类型
StringField  字符串
PasswordField  密码
IntegerField  整数
DecimalField  浮点数，可指定小数点
FloatField   浮点数
BooleanField  布尔值
RadioField
SelectField
DatetimeField

各种的验证
DataRequired  内容是否为空
EqualTo   和谁进行校验
IPAddress   IP地址校验
Length    内容长度校验
NumberRange     数字长度
URL    url校验
Email   邮箱校验
Regexp  正则校验


使用：
    1.安装：
        pip install Flask-WTF
    2.定义form.py文件
        定义一个表单类
        class UserForm(FlaskForm):
            """
            创建一个用户表单
            """
            name = StringField('name', validators=[DataRequired()])

    3.使用:
        视图中：
            form = UserForm()
            return render_template('xx.html', form=form)

       模板中：
        <form action="{{ url_for('hello_world') }}" method="post">
            {{ uform.csrf_token }}  {# 添加csrf保护 #}
            <p>用户名&nbsp;&nbsp;{{ uform.name }} {% if uform.name.errors %} {{ uform.name.errors.0 }} {% endif %}</p>
            <p> 密码&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ uform.password }} {% if uform.password.errors %}{{ uform.password.errors.0 }}{% endif %}</p>
            <p><input type="submit" value="提交"></p>
        </form>

      bootstrap中：
        {% extends 'bootstrap/base.html' %}
        {% import 'bootstrap/wtf.html' as wtf %}

    4.提交验证
        @app.route('/', methods=['GET', 'POST'])
        def hello_world():
            uform = UserForm()  # 表单类对象
            if uform.validate_on_submit():  ----> 主要通过validate_on_submit()方法进行校验
                print(uform.name)
                print(uform.password)
                return '提交成功'
            return render_template('user.html', uform=uform)

文件上传
    1.定义form
    class UserForm(FlaskForm):
        ....
        # 文件上传使用FileField，使用FileRequired()校验，使用FileAllowed限制上传文件的类型
        # 用户头像
        # FileRequired 内容不能为空  FileAllowed 文件上传扩展名列表
        icon = FileField(label='用户头像', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'bmp', 'PNG', 'JPG', 'BMP','GIF', 'BMP', 'JPEG'],
                    message='必须是jpg, png, jpeg, bmp, gif, PNG, JPG, JPEG, BMP, GIF格式的文件')])


    2.模板中使用同其他类型的字段，但是必须在form上面添加：enctype:multipart/form-data

    3.视图函数中如果验证成功，通过以下方式保存：
        icon = uform.icon.data   # icon是FileStorage类型
        filename = secure_filename(icon.filename)  # 文件名
        print('上传的文件名是：------------->', filename)
        print(name, password, phone)
        print(type(icon))  # <class 'werkzeug.datastructures.FileStorage'>

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 绝对路径
        STATIC_DIR = os.path.join(BASE_DIR, 'static')   # 静态文件路径
        UPLOAD_DIR = os.path.join(STATIC_DIR, 'upload')  # 文件上传路径
        icon.save(os.path.join(UPLOAD_DIR, filename))   # 文件保存

    4.