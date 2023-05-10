# import os
import json
import requests


def create_data(tail):
    # fiat, asset = tail[0:2]
    # return asset+fiat
    return tail.asset + tail.fiat

def bnb_main_request(tail):
    symbol = create_data(tail)
    r = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=' + symbol)
    # with open(os.path.dirname(__file__) + 'sbr.xml', 'w') as j:
    #     print(r.text, file=j)  # записываем строку в файл

    return r.json()




