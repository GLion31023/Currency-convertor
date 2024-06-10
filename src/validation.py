from config import load_supported_currencies


def get_valid_amount():
    while True:
        # user is prompted to add an amount (float number with up to two decimal places) or type END to exit
        user_input = input()
        if user_input.upper() == 'END':
            print("Exiting application.")
            return None

        try:
            amount = float(user_input)
            if round(amount, 2) != amount:
                raise ValueError
            return amount
        except ValueError:
            print("Please enter a valid amount")


def get_valid_currency():
    while True:
        # the user is prompted to select one of the supported currencies (3 letters currency code) or type END to exit
        user_input = input()

        if user_input.upper() == 'END':
            print("Exiting application.")
            return None

        currency_code = user_input.strip().upper()
        supported_currencies = load_supported_currencies()
        if currency_code in supported_currencies:
            return currency_code
        else:
            print(f"Please enter a valid currency code")
