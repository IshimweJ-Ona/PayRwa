import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("EXCHANGE_API_KEY")

def convert_currency(data):
    from_curr = data['from']
    to_curr = data['to']
    amount = float(data['amount'])

    url = f"https://v6.exchangenerate-api.com/v6/{API_KEY}/pair/{from_curr}/{to_curr}/{amount}"
    headers = {
        'Authorization': "Bearer " + API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.get(url)
    if response.status_code == 200:
        res = response.json()
        return {'converted': res['conversion_result'],
                'rate': res['conversion_rate']}
    return {'error': 'Conversion failed'}
