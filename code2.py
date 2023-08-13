import requests

def currency_converter(amount, from_currency, to_currency, api_key):
    url = f"https://api.apilayer.com/exchangerates_data/exchange_rates?base={from_currency}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        raise ValueError(f"API error: {data['error']['info']}")

    try:
        exchange_rate = data[to_currency]
    except KeyError:
        raise ValueError(f"Invalid currency code: {to_currency}")

    converted_amount = amount * exchange_rate
    return converted_amount

if __name__ == "__main__":
    api_key = "7fd2a38e6ae665a1ff324c1f031b5771"
    amount = float(input("Enter amount: "))
    from_currency = input("Enter from currency: ").upper()
    to_currency = input("Enter to currency: ").upper()

    converted_amount = currency_converter(amount, from_currency, to_currency, api_key)
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")


