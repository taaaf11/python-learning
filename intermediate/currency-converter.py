import requests

API_KEY = "f584e8a381-4284f16e78-srvf92" # Expires on (25th February, 2025)
BASE_URL = f"https://api.fastforex.io/fetch-one"

def currency_converter(amount, from_currency, to_currency):
    URL = f"{BASE_URL}?from={from_currency}&to={to_currency}&amount={amount}&api_key={API_KEY}"
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        rate = data["result"][to_currency]
        converted_amount = amount * rate
        return converted_amount
    else:
        print("Error fetching data.")
        return None

amount = float(input("Enter the amount you want to convert: "))
from_currency = input("Enter the currency you want to convert from: ").upper()
to_currency = input("Enter the currency you want to convert to: ").upper()

converted_amount = currency_converter(amount, from_currency, to_currency)

if converted_amount is not None:
    print(f"{amount}{from_currency} in {to_currency} is {converted_amount:.2f}")
else:
    print("Error converting currency.")

