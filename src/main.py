import argparse
from datetime import datetime

import validation as v
from config import load_config
from converter import CurrencyConverter
from helpers import next_conversion


def main():
    parser = argparse.ArgumentParser(description="Currency Conversion")
    parser.add_argument('date', type=lambda s: datetime.strptime(s, '%Y-%m-%d'),
                        help="Date for the conversion rates in the format YYYY-MM-DD")

    args = parser.parse_args()
    config = load_config()

    converter = CurrencyConverter(api_key=config['api_key'], date=args.date)

    while True:
        amount = v.get_valid_amount()
        if not amount:
            break

        base_currency = v.get_valid_currency("base currency")
        if not base_currency:
            break

        target_currency = v.get_valid_currency("target currency")
        if not target_currency:
            break

        result = converter.convert(int(amount), base_currency, target_currency)
        print(f"{amount:.2f} {base_currency} is {result} {target_currency}")

        if not next_conversion(converter):
            break


if __name__ == "__main__":
    main()
