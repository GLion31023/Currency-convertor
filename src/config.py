import json


def load_config():
    # read the API key saved in a separate config.json file as per requirement
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config


def load_supported_currencies():
    # load the supported currencies, the list is taken from the FASTForex website
    with open('supported_currencies.json', 'r') as file:
        data = json.load(file)
    return set(data['supported_currencies'])
