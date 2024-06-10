from config import load_supported_currencies


def get_valid_amount():
    while True:
        user_input = input("Enter an amount or type 'END' to exit: ")
        if user_input.upper() == 'END':
            print("Exiting application.")
            return None

        try:
            amount = float(user_input)
            if round(amount, 2) != amount:
                raise ValueError
            return amount
        except ValueError:
            print("Please enter a valid float number with up to two decimal places. Example: 10.23")


def get_valid_currency(currency_type):
    while True:
        user_input = input(f"Enter {currency_type} code or type 'END' to exit: ")

        if user_input.upper() == 'END':
            print("Exiting application.")
            return None

        currency_code = user_input.strip().upper()
        supported_currencies = load_supported_currencies()
        if currency_code in supported_currencies:
            return currency_code
        else:
            print(f"{currency_code} is not a valid currency code. "
                  f"Please enter a valid currency code in ISO 4217 three letter currency code format., e.g., USD.")
