import requests

BASE_URL = 'https://api.exchangerate.host/latest'

def get_exchange_rate(base_currency: str, target_currency: str):
    url = f'{BASE_URL}?base={base_currency}'
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print("Error fetching data from the API.")
        return None
    
    if 'rates' in data and target_currency in data['rates']:
        return data['rates'][target_currency]
    else:
        print(f"Currency {target_currency} is not available.")
        return None

def convert_currency(amount: float, base_currency: str, target_currency: str):
    rate = get_exchange_rate(base_currency, target_currency)
    
    if rate:
        converted_amount = amount * rate
        print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        return converted_amount
    else:
        print("Currency conversion failed.")
        return None

if __name__ == "__main__":
    try:
        amount = float(input("Enter the amount you want to convert: "))
        base_currency = input("Enter the base currency code (e.g., USD): ").upper()
        target_currency = input("Enter the target currency code (e.g., EUR): ").upper()

        convert_currency(amount, base_currency, target_currency)
    except ValueError:
        print("Please enter a valid amount.")
