# Currency Convertor CLI

## Overview
This Currency Converter is a command-line interface application that provides real-time and historical currency conversion using the FastForex API. It supports conversions between a wide range of currencies under the constraints of a trial API key, which allows fetching historical data up to 14 days from the current date.


## Installation
Clone the repository to your local machine:
```
git clone https://github.com/GLion31023/Currency-convertor.git
```
cd currency-converter

Install the required Python packages:
```
pip install -r requirements.txt
```

## Configuration
- API Key: The application requires a FastForex API key. Place your API key in the config.json file as follows:
```
{
  "api_key": "your_api_key_here"
}
```
- Supported Currencies: The application uses a supported_currencies.json file to validate input currencies, which should list all supported currency codes.


## Features
- Real-time currency conversion.
- Historical currency conversion for up to 14 days from today.
- Caching of currency conversion rates to optimize API usage.
- Saving conversion results into a JSON file.


## Usage
Run the application from the command line by navigating to the project's root directory and using the following command:

```
python CurrencyConversion.py YYYY-MM-DD
```

- YYYY-MM-DD: The date for which you want to fetch the conversion rates. This date should be within the last 14 days.


## Commands
All user promts are developed without labels (as per project requirements) 
- Amount: Enter the amount you wish to convert. You must enter a valid float number.
- Curr code: Enter the 3-letter currency code for both the base and target currencies as prompted.
- Continue Conversion: After each conversion, you can choose to continue by typing 'YES' or exit by typing 'END'.


## Project Structure
```
currency-converter-project/
│
├── src/                         - Contains all source files.
│   ├── config.py                - Module to load configuration settings.
│   ├── converter.py             - Contains the CurrencyConverter class handling API interactions.
│   ├── helpers.py               - Includes helper functions for conversion and file management.
│   └── validation.py            - Contains functions to validate user inputs.
│
├── CurrencyConversion.py        - The executable file (main.py) that runs the application (named as per the project requirements).
├── conversions.json             - Stores the history of conversion operations.
├── config.json                  - Stores configuration details such as the API key.
└── supported_currencies.json    - Lists all currencies supported by the API.
```
