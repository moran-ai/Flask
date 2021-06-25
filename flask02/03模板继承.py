from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def test():
    return render_template('child.html')


@app.route('/t')
def test1():
    return render_template('include.html')


if __name__ == '__main__':
    app.run(debug=True)
