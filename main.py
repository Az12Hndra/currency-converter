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
    
def get_user_input(rates):
    while True:
        to_currency = input('Enter the currency you want to convert to (e.g EUR): ').upper()
        amount = float(input('Enter the amount you want to convert: '))

        if to_currency not in rates:
            print('Invalid currency code. Please try again.')
            continue
        else:
            break
        
    return to_currency, amount

def convert(rates, to_currency, amount):
    if to_currency not in rates:
        print('Invalid target currency code. Please try again.')
        return None
    
    conversion_rate = rates[to_currency]
    result = conversion_rate * amount
    return result

def display_result(amount, from_currency, result, to_currency):
    print(f'{amount} {from_currency} = {result:,.2f} {to_currency}')
    
def main():
    print('Welcome to Currency Converter')
    print('~' * 29)

    from_currency = input('Enter the currency you want to convert from (e.g USD): ').upper()
    rates = get_rates(from_currency)
    to_currency, amount = get_user_input(rates)
    result = convert(rates, to_currency, amount)
    display_result(amount, from_currency, result, to_currency)

main()
