from flask import Flask, request
import logging
import requests

app = Flask(__name__)

def getdata(pincode,date):
    headersc = {
    'authority': 'cdn-api.co-vin.in',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.8.107.794 Safari/537.36',
    'origin': 'https://www.cowin.gov.in',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.cowin.gov.in/home',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'if-none-match': 'W/"7b1e-u5AO2iIdcDpbt4Qo1JbYPHtUqx8"',
}
    # url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+pincode+"&date="+date
    url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode={pincode}&date={date}'
    reposne_data = None
    try:
        reposne_data = requests.request(
            "GET", url,  headers=headersc, timeout=150
        ).json()
    except Exception as e:
        logging.debug(f"Error is {e}")
        print("API calling error")

    print(type(reposne_data))    
    if reposne_data != None:
        if not 'centers' in reposne_data or len(reposne_data['centers']) == 0:
            return "No data of Centers for this date and pincode"
        else:
            return reposne_data
    else:
        return "CoWin API calling error"


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
    if not 'pincodes' in data or not 'dateArr' in data or len(data['pincodes']) == 0 or len(data['dateArr']) == 0:
        logging.debug("Input is missing")
        data = "Missing inputs"
    else:
        pincode = str(data['pincodes'])
        date = data['dateArr']
        data = getdata(pincode,date)

    return data


if __name__ == '__main__':
    app.run()

    