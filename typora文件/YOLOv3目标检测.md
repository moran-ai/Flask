# YOLOv3目标检测

```python
安装所需的依赖包
pip install flask
pip install opencv-python
pip install keras
pip install tensorflow
pip install numpy

# flask代码实现部分
import os
from flask import Flask, render_template, url_for, request, jsonify

# 创建app
app = Flask(__name__)

path = '目标检测图片存放路径'

# 支持上传的文件格式
ALLOWED_FILENAME = ['jpg', 'png', 'bmp', 'gif', 'BMP', 'GIF', 'PNG', 'JPG']

# 创建上传图片路由
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # 获取上传的文件
        file = request.files.get('file')
        # 获取文件名
        f_name = file.filename
        
        # 取出文件后缀名
        t_name = f_name.rsplit('.')[-1]
        
        if t_name in ALLOWED_FILENAME:
            file_path = os.path.join('上传文件的保存路径', f_name)
            file.save(file_path)
            return render_template('upload_ok.html')
        else:
            return jsonify({"error": '1001', 'msg':'仅支持bmp, png, gif, jpg, BMP, GIF, PNG, GIF格式的文件，请重新选择'})
    return render_template('upload.html')

if __name__ == '__main___':
    app.run()
```

