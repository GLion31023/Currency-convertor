import requests

from datetime import datetime
from src.helpers import save_conversion


class CurrencyConverter:
    def __init__(self, api_key, date):
        self.api_key = api_key
        self.date = date.date() if isinstance(date, datetime) else date
        self.rates_cache = {}

    def get_rates(self, base_currency, target_currency):
        """ Gets the conversion rate for the currency pair either from the API response or from the cache.
        Uses two different endpoints:
        - Historical for any date in last 14 days (due to trial key limitations)
        - Fetch one - for instances where the date is today, but time is before 16:00 UK time ( as historical does
         not support request before this time for the same day)
         """

        today = datetime.now().date()
        local_time = datetime.now().time()

        cache_key = (base_currency, target_currency, str(self.date))

        if cache_key in self.rates_cache:  # Gets the cached exchanged rate if already available
            return self.rates_cache[cache_key]

        if self.date == today and local_time < datetime.strptime("18:00", "%H:%M").time():
            url = f"https://api.fastforex.io/fetch-one?from={base_currency}&to={target_currency}&api_key={self.api_key}"
            json_key = 'result'  # There is a difference in the json response when we call the different endpoints
        else:
            url = (f"https://api.fastforex.io/historical?date={self.date}&from={base_currency}&to={target_currency}"
                   f"&api_key={self.api_key}")
            json_key = 'results'

        response = requests.get(url)
        data = response.json()
        result = data[json_key][target_currency]

        self.rates_cache[cache_key] = result

        return result

    def convert(self, amount, base_currency, target_currency):
        """ Executes and saves the successful conversion with the provided data."""
        rate = self.get_rates(base_currency, target_currency)

        if rate is not None:
            converted_amount = round(amount * rate, 2)
            conversion_data = {
                "date": self.date.strftime("%Y-%m-%d"),
                "amount": amount,
                "base_currency": base_currency,
                "target_currency": target_currency,
                "converted_amount": converted_amount
            }

            save_conversion(conversion_data)

            return converted_amount
