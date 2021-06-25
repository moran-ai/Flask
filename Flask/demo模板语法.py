from flask import Flask
from flask import render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)

class Girl:
    def __init__(self, name, addr):
        self.name = name
        self.gender = '女'
        self.addr = addr

    def __str__(self):
        return self.name + ', '+self.gender + ', '+self.addr

@app.route('/show')
def show():
    name = '王琦'
    age = 18
    l = ['a', 'b', 'c', 'd']
    dict1 = {'a':'a', 'b':'b', 'c':'c'}
    yuanzu = (10, 34)
    # 创建girl对象
    girla = Girl('王五','中国')

    # 如果没有找到，则以空白字符串填充
    return render_template('show.html',name=name, age=age,gender='男', l=l,
                           dict1=dict1,girla=girla, yuanzu=yuanzu)

if __name__ == '__main__':
    app.run()
