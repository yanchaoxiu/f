
from flask import Flask
app = Flask(__name__)
CSRF_ENABLED=True
SERVER_KEY='you will-never-guess'
app.config.from_object('config')
@app.route('/')
def hello_world():
    return 'Hello Xiuxiu!'


if __name__ == '__main__':
    app.run()
