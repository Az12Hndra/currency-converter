import requests
import json

def get_rates(from_currency):
    api_key = '71ae59f702af30bf3184d6c4'
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'
    response = requests.get(url)
    data = response.json()

    # print(json.dumps(data, indent=4))

    if data['result'] != 'success':
        print('Failed to fetch exchange rates. Check your internet connection and API key.')
        return None
    
    return data['conversion_rates']
    
def get_user_input():
    pass

def convert(rates, to_currency, amount):
    pass

def display_result():
    pass
