from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_name():
    return 'Hello!!!!!!!1'


if __name__ == '__main__':
    app.run()