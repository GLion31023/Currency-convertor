import json


def load_config():
    """ Reads the API key from the json file. """
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config


def load_supported_currencies():
    """ Get the supported currencies. """
    with open('supported_currencies.json', 'r') as file:
        data = json.load(file)
    return set(data['supported_currencies'])
