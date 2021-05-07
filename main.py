from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_name():
    return 'Hello!!!!!!!1'



@app.route('/test')
def hello_name():
    return 'Test2'

if __name__ == '__main__':
    app.run()