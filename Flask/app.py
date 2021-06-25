from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)

# 所有的路由搜索规则都是自上而下搜索,在写路由时定义的路由是唯一的
@app.route('/')
def hello_world():
    return 'Hello World!'

# 路由中定义'/',无论请求的url是否带有/，都可以执行视图函数
# 如果请求不带/，那么浏览器做了一次重定向
@app.route('/projects/')  # 请求路由不写第二个/，也正确
def projects():
    return 'The projects page'

@app.route('/about')  # 如果请求路由中写/about/，会出现Not Found
def about():
    return 'The about page'

if __name__ == '__main__':
    app.run()
