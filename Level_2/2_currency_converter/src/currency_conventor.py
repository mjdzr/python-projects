import requests


# Define a function to get exchange rates
def get_exchange_rate(base_currency, target_currency):
    url = f'https://api.exchangerate-api.com/v4/latest/{base_currency}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['rates'][target_currency.upper()]
    elif response.status_code == 404:
        print("Error 404: The requested resource was not found.")
        return None
    elif response.status_code == 500:
        print("Error 500: Internal server error. Please try again later.")
        return None
    else:
        print(f"Error: Received unexpected status code {response.status_code}.")
        return None

# Define a function that converts the currency
def currency_converter(base_amount, exchange_rate):
        return base_amount * exchange_rate


# Get currency list
def currency_list():
    url = f'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    return list(data['rates'])

# main
if __name__ == "__main__":
    base_amount = float(input('Please provide the amount you want to convert:\n'))
    base_currency = input('Please provide the currency of the amount you have provided:\n')
    target_currency = input('Please enter the currency you want to convert to:\n')
    print(currency_converter(base_amount, base_currency, target_currency))