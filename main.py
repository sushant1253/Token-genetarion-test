from flask import Flask, request

app = Flask(__name__)


@app.route('/hello')
def hello_name():
    return 'Hello!!!!!!!1'



@app.route('/test')
def test():
    return 'Test'


@app.route('/test2')
def test2():
    return 'Test2'


@app.route('/center')
def getCenters():
    data= request.get_json(force=True)
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode="+data['pincodes']+"&date="+data['dateArr']
    return data['pincodes']


if __name__ == '__main__':
    app.run()