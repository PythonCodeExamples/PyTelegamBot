'''
Small parser for test bot's functionality.
NOT FOR COMMERCIAL USAGE.
'''

import requests


def parse_bitcoin():
    BITCOIN_PRASE_URL = "https://blockchain.info/ticker"
    res = requests.get(BITCOIN_PRASE_URL)
    return str(res.json()["USD"]["15m"]) + "$"


''' Sample test'''
if __name__ == "__main__":
    print(parse_bitcoin())

