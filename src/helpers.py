from datetime import datetime


def next_conversion(converter):
    while True:
        # the user is expected to continue with yes/end
        new_conversion = input().strip().upper()

        if new_conversion.upper() == 'END':
            print("Exiting application.")
            return False
        elif new_conversion == 'YES':
            # The user is asked if they want to change the current date, expected to proceed with yes/no
            new_date = input().lower()
            if new_date == 'yes':
                if not change_date(converter):
                    return False
            return True
        else:
            print("Invalid response. Please type 'YES' to continue or 'END' to exit.")


def change_date(converter):
    while True:
        # the user is prompted to enter a new date, it has to be within 14 days due to trial API key limitations
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
