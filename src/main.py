import argparse
from datetime import datetime

import validation as v
from config import load_config
from converter import CurrencyConverter


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

        new_date_input = input("Enter another date in format YYYY-MM-DD to continue, or 'END' to exit: ")
        if new_date_input.upper() == 'END':
            print("Exiting application.")
            break
        try:
            new_date = datetime.strptime(new_date_input, '%Y-%m-%d')
            converter.date = new_date
        except ValueError:
            print("Invalid date format. Please enter a valid date in the format YYYY-MM-DD.")
            continue


if __name__ == "__main__":
    main()
