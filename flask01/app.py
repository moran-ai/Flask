from flask import Flask

app = Flask(__name__, static_url_path='/h')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
