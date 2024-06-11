import argparse

from datetime import datetime

from src.config import load_config
from src.converter import CurrencyConverter
from src.helpers import next_conversion
from src.validation import get_valid_amount, get_valid_currency


def parse_arguments():
    """ Parse the command line argument. """
    parser = argparse.ArgumentParser(description="Currency Conversion")
    parser.add_argument('date', type=lambda s: datetime.strptime(s, '%Y-%m-%d'),
                        help="Date for the conversion rates in the format YYYY-MM-DD")

    return parser.parse_args()


def setup_converter(args):
    """ Set up the currency converter with the API key and date. """
    config = load_config()
    return CurrencyConverter(api_key=config['api_key'], date=args.date)


def print_result(amount, base_currency, result, target_currency):
    """ Prints the end result """
    bold_start = '\033[1m'
    bold_end = '\033[0m'
    print(f"{bold_start}{amount:.2f} {base_currency} is {result} {target_currency}{bold_end}")


def run_process(converter):
    """ Manages the process of converting currencies based on the input information. """
    while True:
        amount = get_valid_amount()
        if not amount:
            break

        base_currency = get_valid_currency()
        if not base_currency:
            break

        target_currency = get_valid_currency()
        if not target_currency:
            break

        result = converter.convert(int(amount), base_currency, target_currency)
        print_result(amount, base_currency, result, target_currency)

        if not next_conversion(converter):
            break


def currency_conversion():
    """ The main function that runs the currency conversion application. """
    args = parse_arguments()
    converter = setup_converter(args)
    run_process(converter)


currency_conversion()
