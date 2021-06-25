from flask import Flask
from flask import request
from flask import render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)

@app.route('/')
def index():
    return

if __name__ == '__main__':
    app.run()