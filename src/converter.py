import requests


class CurrencyConverter:
    def __init__(self, api_key, date):
        self.api_key = api_key
        self.date = date
        self.rates_cache = {}

    def get_rates(self, base_currency, target_currency, date=None):

        cache_key = (base_currency, target_currency)

        if cache_key not in self.rates_cache:
            response = requests.get(f"https://api.fastforex.io/fetch-one?from={base_currency}&to={target_currency}"
                                    f"&api_key={self.api_key}")
            data = response.json()
            print("API Response: ", data)

            print(data['result'][target_currency])

            return data['result'][target_currency]

    def convert(self, amount, base_currency, target_currency):
        rate = self.get_rates(base_currency, target_currency)
        return round(amount * rate, 2)
