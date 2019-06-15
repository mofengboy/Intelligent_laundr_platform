from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/authentication')
def authentication():

    return 'AuthenticationTest'


if __name__ == '__main__':
    app.run()
