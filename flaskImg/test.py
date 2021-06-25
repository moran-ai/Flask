from flask import request, render_template, Flask

app = Flask(__name__)


@app.route('/test')
def hello():
    data = request.args.get('data')
    print(data)
    return render_template('test.html')


@app.route('/test1', methods=['GET', 'POST'])
def test():
    data = request.args.get('data')
    print(data)
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
