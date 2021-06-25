# Flask开发

# Flask的Flask-WTF使用

## **1.Flask-WTF的安装**

```
pip install Flask-WTF
```



## **2.Flask-WTF的文档地址**

[Flask-WTF文档地址](https://flask-wtf.readthedocs.io/en/stable/)

[pillow地址](https://pillow.readthedocs.io/en/stable/reference/ImageDraw.htm)

[jquery cdn地址](https://cdn.baomitu.com/jquery)



## **3.flask-wtform**

flask-wtform集成了wtform, csrf的保护和文件上传功，图片验证码

## **4.使用步骤**

- ### 安装

  - ```
    pip install Flask-WTF
    ```

    

- ### 构建form.py表单文件

  - ​	**form.py**

    ```python
    # 导入所需的包
    import re
    from flask_wtf import FlaskForm
    from flask_wtf.file import StringField, PasswordField
    from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
    
    # 构建表单类
    # 必须继承FlaskForm父类
    class UserForm(FlaskForm):
        # 用户名
        name = StringField(label='用户名', validators=[DataRequired(), Length(min=6, max=12, message='用户名必须在6~12位之间')])
        # 密码  
        password = PasswordField(lable='密码', validators=[DataRequired(), Length(min=6, max=12, message='密码长度必须在6~12位之间')])
        # 确认密码
        repassword = PasswordField(label='确认密码', validators=[DataRequired(), Length(min=6, max=12, message='密码长度必须在6~12位之间'), EqualTo('password', message='两次密码不一致')])
        # 手机号码
        phone = StringField(label='手机号码', valditaors=[DataRequired(), 
                                                     Length(miin=11, max=11, message='手机号码长度必须为11位')])
        
        # 使用图形验证码  使用
        code = StringField(label='验证码')
        
        # 自定义方法，验证用户名是否符合规范
        def validate_name(self, data):
            # 获取输入的用户名
            """
            type(data) == type(self.data)
            获取输入框的值的方式有两种：
            	1.data.data
            	2.self.name.data
            """
            print('self.name.data的值是-------->', self.name.data)
            print('data.data的值是-------------->', data.data)
            # 判断用户名是否是以数字开头，如果是，则返回异常处理的结果
            # 使用isdigit()方法  isdigit()检查字符串是否只由数字组成
            if self.name.data[0].isdigit():
                # 使用python关键字rasie 抛出异常  ValidationError异常需要导入
                raise ValidationError('用户不能以数字开头')
                
        # 自定义方法，使用正则表达式验证手机号是否以规定的数字开头
        def validate_phone(self, data):
            phone = data.data
            re.search(r'^1[3456789]\d{9}$', phone)
        	raise ValidationError('手机格式不正确')    
        
        # 自定义方法，验证验证码是否一致
        def validate_code(self, data):
            # 获取输入的验证码
            input_code = data.data
            # 获取存储在session中的验证码
            code = session.get('vailcode')
            if input_code.lower() != code.lower():
                raise ValidationError('验证码错误')
    ```

- #### **构建模板文件**

  user.html

  ```html
  <!DOCTYPE html>
  <html lang='en'>
     <head>
         <meta charset='utf-8'>
         <title>flask-form表单使用</title>
         <style>
             p span{
                 font-size: 14px;
                 color: red;
             }
         </style>
         <!-- 从网页服务器上加载jquery ,能提高效率 -->
         <!-- 使用javascript脚本随机改变图形验证码 -->
         <script src='https://lib.baomitu.com/jquery/3.5.1/jquery.min.js'></script>
      </head>
      <body>
          <!--使用url_for()重定向到指定的路由 -->
          <form action='{{url_for("hello_word")}}', method='post' enctype='multipart/form-data'>
               <!--添加csrf保护 -->
              {{uform.csrf_token}}
              <p>{{uform.name.label}}: {{uform.name}}<span>{% if ufrom.name.erros %}{{uform.name.erros.0}}{% endif %}</span></p>
               <p>{{uform.password.label}}: {{uform.password}}<span>{% if ufrom.password.erros %}{{uform.password.erros.0}}{% endif %}</span></p>
              <p>{{uform.repassword.label}}: {{uform.repassword}}<span>{% if ufrom.repassword.erros %}{{uform.repassword.erros.0}}{% endif %}</span></p>
              <p>{{uform.phone.label}}: {{uform.phone}}<span>{% if ufrom.phone.erros %}{{uform.phone.erros.0}}{% endif %}</span></p>
               <p>{{uform.code.label}}: {{uform.code}} <img src='{{url_for("get_img")}}' alt='' id='img'></p>
              <p><span>{% if ufrom.code.erros %}{{uform.code.erros.0}}{% endif %}</span></p>
    			<p><input type='submit' value='提交'></p>
          </form>
          <!-- 随机改变验证码-->
          <script>
          	$('#img').click(function(){
                  // 改变验证码，点击改变src的值  点击验证码图片向服务器重新发送一次请求 Math.random()随机数
  				$(this).attr('src', '{{url_for("get_image")}}?ran=' + Math.random())
              })
          </script>
      </body>
  </html>
  ```

  - **构建启动文件**

    app.py

    ```python
    import session
    from flask import Flask, render_template
    from form import Userform  # 导入自定义的表单
    from flask_wtf import CSRFProtect   # 全局csrf保护
    from util import generate_iamge
    from io import BytesIO
    
    app = Flask(__name__)
    '''
    配置app的配置文件
    配置SECRET_KEY密钥，作用提供CSRF保护
    配置CSRF全局保护的作用是，防止数据被恶意篡改,防止网站攻击
    '''
    app['ENV'] = 'development'
    app['DEBUG'] = True
    app['SECRET_KEY'] = 'qweeadf1234567'  # 自定义赋值
    
    # 验证码处理
    app.config['RECAPTCHA_PUBLIC_KEY'] = 'rerewrerwerrtreteeqwr5767'  # 公钥
    app.config['RECAPTCHA_PRIVATE_KEY'] = 'sfsdfsdfw456789gsdgfsfsad'  # 私钥
    app.config['RECAPTCHA_PARAMETERS'] = {'h1': 'zh', 'render': 'explicit'}
    app.config['RECAPTCHA_DATA_ATTRS'] = {'theme': 'dark'}
    # 配置全局的CSRF保护 需要导入依赖包
    csrf = CSRFProtect(app=app)
    
    @app.route('/', methods=['GET', 'POST'])
    def hello_word():
        # 导入定义的表单
        uform = Userform()  
        	
        # 使用validate_submit()函数  
        # validate_submit() 处理逻辑的操作，等效于if request.method=='POST' and from.validate():
        if uform.validate_on_submit():
            # 获取表单中提交的数据
            name = uform.name.data
        	password = ufrom.name.data
            phone = ufrom.name.data
            return '提交成功'
        return render_tempalte('user.html')
    
    # 将图形验证码转为二进制
    @app.route('/image')
    def get_iamge():
        img, code = generate_image(6)
        
        # 将图片转为二进制
        buffer = BytesIO()  # 创建一个二进制容器
    	img.save(buffer, 'JPEG')
        # 获取容器中的值
        buf_bytes = buffer.getvalue()  
        # 保存验证码到session
        session['vailcode'] = code
        # 使用make_response()构建response对象
    	response = make_response(buf_bytes)
        
        # 设置请求头类型
        response.headers['Content-Type'] = 'image/jpg'
        return response 
    ```
    
    

- **绘制图形验证码**

  util.py

  ```python
  '''
  flask中的flask_wtf图形验证码的模块RecaptchaField的底层公钥和私钥默认使用谷歌API, 不方便使用
  from flask_wtf import RecaptchaField
  '''
  '''
  绘制验证码使用的依赖包：
  	pillow: PIL的替代版本，处理图像, 调用里面的Image API
  	random: 随机产生验证码
  	PIL：处理图片
  pillow 需要安装
  pip install pillow
  '''
  import random
  from PIL import Image, ImageFont, ImageDraw, ImageFilter
  
  # 随机产生图形验证码的颜色
  def generate_random_coloe():
      '''
      随机产生三通道的颜色
      '''
      return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
  
  # 生成图片
  def generate_img(length):
      '''
      length:图形验证码的长度
      '''
      # 用来随机产生验证码的序列
      s = 'qweAFAF12334fa35656sdfaD34ASsD557dfW6E7WQwE'
      
      # 创建画布
      # 指定图片的大小
      size = (128, 50)  # 图片大小
      # 使用Image.new()创建画布  Image.new()参数：图片模式，图片大小，图片颜色
      img = Image.new('RGB', size=size, color=generate_random_color())
      # 创建字体，使用ImageFont.truetype(path, size)  字体路径和字体大小
      font = ImageFont.truetype('C:\Windows\Fonts\simhei.ttf', size=40)
      # 画验证码  ImageDraw.Draw(img, model) 参数解析：img:绘制图片的位置， model：模式(BGR, RGB)可选
      draw = ImageDraw.Draw(img)
      # 绘制验证码
      code = ''
      for i in range(length):
          c = random.choice(s) # 随机选择文字
          code += c  # 验证码
          # 写入文字 text(x：横轴, y：纵轴, fill:颜色, font:字体)
          draw.text((5 + random.randint(4, 7) + 20 * i, random.randint(5, 9)), text=c, fill=generate_random_color(), font=font)
      
      # 绘制干扰线
      for i in range(20):
          x1 = random.randomint(0, 130)
          y1 = random.randomint(0, 50 / 2)
          
          x2 = random.randomint(0, 130)
          y3 = random.randomint(50 / 2, 130)
          draw.line((x1, y1), (x2, y2), fill=generate_random_color())
      	
      # 添加滤镜
  	img = img.filter(ImageFilter.EDGE_ENHANCE)
      return img, code
  ```
  
  