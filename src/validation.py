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
        if currency_code in supported_currencies:
            return currency_code
        else:
            print(f"{currency_code} is not a valid currency code. "
                  f"Please enter a valid currency code in ISO 4217 three letter currency code format., e.g., USD.")


supported_currencies = {
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD",
    "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BZD",
    "CAD", "CDF", "CHF", "CLF", "CLP", "CNH", "CNY", "COP", "CUP", "CVE", "CZK", "DJF",
    "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS",
    "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS",
    "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW",
    "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL",
    "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN",
    "NAD", "NGN", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN",
    "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SCR", "SDG", "SEK", "SGD", "SHP",
    "SLL", "SOS", "SRD", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD",
    "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VND", "VUV", "WST", "XAF", "XCD",
    "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW"
}
