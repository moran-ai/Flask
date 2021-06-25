# Flask文件上传

```python
'''
安装：pip install flask
'''
# 导入所需的包文件
import os
from flask import Flask, render_template, url_for, redirct, request, jsonify, secure_filename
# 创建app
app  = Flask(__name__, template_folder='xxxpath')
# 设置上传图片的目录
UPLOAD_FOLDER = 'xxxpath'
#将上传图片的目录加入配置文件
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# 设定文件上传的格式
ALLOWERD_UPOLAD = ['jpg', 'png', 'bmp', 'gif']

# 判断上传的文件的后缀名是否符合要求
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[-1] in ALLOWERD_UPLOAD

# 上传图片的路由
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.methods == 'POST':
        file = request.files.get('file')
        if file not in allowed_file(file.filename):
            return jsonify({'error': 1001, 'msg': '文件的类型仅限于jpg, png, bmp, gif,请重新选择'})
        if file and allowed_file(file.filenmae) :	
            filename = secure_filename(file.filename)
            # 文件的保存
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('upload.html', filename=filename)
    return render_template('upload.html')
```

# Flask文件下载

```python
'''
所需要的函数：
from flask import send_from_directory
'''
# 导入所需的包文件
from flask import Flask, send_from_directory, request, render_template

# 创建app
app = Flask(__name__, template_folder='xxx')

# 创建文件下载的路由  传入参数filename:filename为所需下载的文件名
@app.route('/download_file/<filename>')
def download_filename(filename):
    return send_from _directory(app.config['UPLOAD_FOLDER'], filename)
```

# 使用Flask+ajax上传文件

```html
/*
使用ajax上传文件
*/
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset='UTF-8'>
        <title>upload</title>
        <style>
            
        </style>
        <script src='static/js/jQuery-min.js'></script>
        <script type='text/javascript'>
        	$(function(){
                // 选择文件的事件
                $('#btn').click(function(){
                    $('#obj').click();
                })
                
                // 上传图片
                $('#obj').change(function(){
                    // 创建formData对象
                    var formData = new FomData();
                    
                    // 添加
                    formData.append('file', $('#obj')[0].files[0]);
                    
                    // 获取的上传文件的值
                    var fileobj = $('#obj').value();
                    
                    // 使用ajax 上传图片
                    $.ajax({
						url:'',  // 请求地址
                        type: 'POST',   // 请求方式
                        data: formData,  // 请求传输的数据
                        processData: false,   // jQuery不要去处理发送的数据
                        contentType: false,   // jQuery不要去设置Content-Type的请求头
                        
                        // 成功后执行回调函数
                        success: function(status){
                            // 找到图片的id
                            var img1 = $('#img1');
                            img1.attr('src', status).width(1300).height(589);  // 设置图片的宽高
                        },
                        error: function(){
                            alert('文件上传失败')
                        }
                    });
                });
                
                // 预测图片
                $('#btn2').click(function(data){
					$.ajax({
                        url: '',  // 请求地址 
                        type: 'POST',   // 请求方式
                        data: data,   // 请求数据
                        processData: false,   // jQuery不处理发送的数据
                        contentType: false,   // jQuery不对Content-Type设置请求头
                        success: function(status1){
                            var img2 = $('#img2');
                            img2.attr('src', status1).width(1300).heigth(589);
                        },
                        error: function(){
                            alert('预测失败');
                        }
                    });
                });
            })
        </script>
    </head>
 <body>
 	<div class='box'>
        <input type='file' name='file' id='obj' style="display:none;" value='选择文件'>
        <input type='button' value='选择文件' id='btn' class='btn'>
        <input type='button' value='点击预测' id='btn2' class='btn'>
     </div>
     <div>
         <img src='' alt='' id='img1'>
         <img src='' alt='' id='img2'>
     </div>
 </body>
</html>
```



Flask部分  使用蓝图

__init__.py文件

```python
'''
安装依赖包
pip install flask_script
pip install flask
'''
import settings
from flask import Flask
# 配置app
def create_app():
    app = Flask(__name__, template_filder='../templates', static_fileder='../static')
    # 进行配置文件的导入
    app.config.from_object(settings)
    # 注册蓝图
    app.regsiter_blueprint(blue)  # blue需要从主程序中导入
    
    return app
```



settings.py文件

```python
import os
ENV = 'development'
DEBUG = True

BASE_PATH = os.path.dirname(__file__)
STATIC_DIR = os.path.join(BASE_PATH, 'static')

# 文件上传目录
UPLOAD_DIR = os.path.join(STATIC_DIR, 'img')
```



配置启动文件

```python
from flask_script import Manager
app = create_app()
manager = Manager(app=app)

if __name__ == '__main__':
    manager.run()
```



项目主程序

```python
import settings
import os
from flask import Blueprint, render_template, request, session
from werkzeug.utils import secure_filename
# 创建蓝图 blue为蓝图的名字
blue = Blueprint('blue', __name__)

ALLOWRD_FIELNAME = ['jpg', 'png', 'gif', 'bmp', 'BMP', 'GIF', 'PNG', 'JPG', 'jpeg', 'JPEG']

# 文件上传路由
@blue.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        
        # 文件名
        f = file.filename
        # 设定全局session
        session['f'] = file.filename
        # 判断文件后缀是否符合规范
        f_name = f.rsplit('.')[-1]
        if f_name in ALLOWED_FILENAME:
            secure_filename(f_name)
            f_path = os.path.join(settings.UPLOAD_DIR, f)
            file.save(f_path)
            # 返回图片路径给前端
            return 'static/img/' + f
    return render_template('upload.html')

@blue.route('/yc', methods=['GET', 'POST'])
def yc():
    if request.method == 'POST':
        f = session.get('f')
        # 导入yolov3模型
        
        # 将训练好的图片发送给前端
        return 'static\\predict_img\\' + f
    else:
        return '请求失败'
```

