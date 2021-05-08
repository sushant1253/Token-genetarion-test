import requests
# from utils.helper import gen_tele_msg, get_proxy_pool, send_message
from datetime import datetime, timezone


date = datetime.today().strftime('%d-%m-%Y')

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

pincode = 414001

url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={date}'

response = requests.request(
                "GET", url, headers=headersc, timeout=8).json()

print(response)