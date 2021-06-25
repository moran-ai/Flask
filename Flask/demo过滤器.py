from flask import Flask
from flask import render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)

@app.route('/show2')
def show2():
    girls = ['a', 'b', 'dgc', 'dgh', 'eddd', 'f']
    users = [
        {'name':'安妮', 'password':123456},
        {'name':'安妮1', 'password':123454},
        {'name':'安妮2', 'password':123456},
        {'name':'安3', 'password':123453}
    ]
    msg = '<h1>快乐</h1>'
    n1 = 'hello'
    return render_template('show2.html', girls=girls, users=users,msg=msg, n1=n1)

if __name__ == '__main__':
    app.run()