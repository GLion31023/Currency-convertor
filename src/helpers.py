import json
import os

from datetime import datetime


def next_conversion(converter):
    """ Asks the user if they want to continue with another conversion. """
    while True:
        # the user is expected to continue with yes/end
        new_conversion = input("Would you like to exchange again? (yes/end) ").strip().upper()

        if new_conversion.upper() == 'END':
            print("Exiting application.")
            return False
        elif new_conversion == 'YES':
            # The user is asked if they want to change the current date, expected to proceed with yes/no
            new_date = input("Would you like to change the date? (yes/no) ").lower()
            if new_date == 'yes':
                if not change_date(converter):
                    return False
            return True
        else:
            print("Invalid response. Please type 'YES' to continue or 'END' to exit.")


def change_date(converter):
    """ Allows the user to change the date if they want to check the conversion rate for another day. """
    while True:
        # the user is prompted to enter a new date, within the past 14 days due to trial API key limitations
        new_date_input = input()
        if new_date_input.upper() == 'END':
            print("Exiting application.")
            return False

        try:
            new_date = datetime.strptime(new_date_input, '%Y-%m-%d')
            converter.date = new_date
            return True
        except ValueError:
            print("Please enter a valid date format.")


def save_conversion(conversion_data):
    """ Helper function to save the successful conversions. """
    directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(directory, '..', 'conversions.json')
    try:
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(conversion_data)

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(f'Failed to save data: {e}')
