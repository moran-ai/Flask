from flask import Flask
from flask import render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)

@app.route('/show1')
def show1():
    girls = ['a', 'b', 'dgc', 'dgh', 'eddd', 'f']
    users = [
        {'name':'安妮', 'password':123456},
        {'name':'安妮1', 'password':123454},
        {'name':'安妮2', 'password':123456},
        {'name':'安3', 'password':123453}
    ]
    return render_template('show_1.html', girls=girls, users=users)

if __name__ == '__main__':
    app.run()