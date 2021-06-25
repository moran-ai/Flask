import re
from flask import session
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo, Regexp

class UserForm(FlaskForm):
    """
    创建一个用户表单
    """
    # StringField 对应于input标签中的type属性  'name'对应于input标签中的name属性
    # validators为验证器  DataRequired()检验输入框中是否有内容， Length 确定输入内容的长度
    # 用户名
    name = StringField(label='用户名',validators=[DataRequired(),Length(min=6, max=12, message='用户名长度必须在6~12位之间')])
    # 密码
    password = PasswordField(label='密码',validators=[DataRequired(),Length(min=6, max=12, message='密码长度必须在6~12位之间')])
    # 确认密码
    confirm_pwd = PasswordField(label='确认密码',validators=[DataRequired(),Length(min=6, max=12, message='密码长度必须在6~12之间'),
        EqualTo('password', message='两次密码不一致')])
    # 手机号码
    phone = StringField(label='手机号码',validators=[DataRequired(),Length(min=11, max=11, message='手机号码长度必须为11位')])
    # 用户头像
    # FileRequired 内容不能为空  FileAllowed 文件上传扩展名列表
    icon = FileField(label='用户头像', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'bmp', 'PNG', 'JPG', 'BMP','GIF', 'BMP', 'JPEG'],
                message='必须是jpg, png, jpeg, bmp, gif, PNG, JPG, JPEG, BMP, GIF格式的文件')])

    # 图形验证码
    recaptcha = StringField(label='验证码')

    # 进行验证码的验证
    def validate_recaptcha(self, data):
        # 输入的验证码
        input_code = data.data
        # 存在session中的验证码
        code = session.get('vailcode')
        # 转为小写 lower()
        if input_code.lower() != code.lower():
            raise ValidationError('验证码错误')

    # 自定义验证方法  验证用户名
    def validate_name(self, data):
        # if self.name.data[0].isdigit():
        print('name -------->', self.name.data) # 输入的用户名
        print('data ==========>', data)  # <input id="name" name="name" required type="text" value="qwertgfg">
        if self.name.data[0].isdigit():
            raise ValidationError('用户名不能以数字开头')

    # 自定义验证手机号
    def validate_phone(self, data):
        phone = data.data
        if not re.search(r'^1[356789]\d{9}$', phone):
            raise ValidationError('手机号码格式错误')

