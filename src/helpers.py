from datetime import datetime


def next_conversion(converter):
    while True:
        new_conversion = input("Would you like to continue with another conversion? (YES/END): ").strip().upper()

        if new_conversion.upper() == 'END':
            print("Exiting application.")
            return False
        elif new_conversion == 'YES':
            new_date = input("Would you like to change the date for the next conversion (yes/no): ").lower()
            if new_date == 'yes':
                if not change_date(converter):
                    return False
            return True
        else:
            print("Invalid response. Please type 'YES' to continue or 'END' to exit.")


def change_date(converter):
    while True:
        new_date_input = input("Enter a new date (YYYY-MM-DD) or 'END' to exit: ")
        if new_date_input.upper() == 'END':
            print("Exiting application.")
            return False

        try:
            new_date = datetime.strptime(new_date_input, '%Y-%m-%d')
            converter.date = new_date
            return True
        except ValueError:
            print("Invalid date format. Please enter a valid date in the format YYYY-MM-DD.")
