import requests
import json


def create_data(tail):
    # ('RUB', 'USDT', 'BUY')
    data = {
      # "fiat": tail[0], # "RUB",
      # "asset": tail[1], # "USDT",
      "fiat": tail.fiat, # "RUB",
      "asset": tail.asset, # "USDT",
      "merchantCheck": False,
      "page": 1,
      "payTypes": ["YandexMoney", "RosBank", "ABank", "Tinkoff", "QIWI", "Payeer", "RUBfiatbalance"], #        ЮMoney 
      "publisherType": None,
      "rows": 10,
      "tradeType": tail.tradeType, # "SELL"
    }

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "123",
        "content-type": "application/json",
        "Host": "p2p.binance.com",
        "Origin": "https://p2p.binance.com",
        "Pragma": "no-cache",
        "TE": "Trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
    }
    return headers, data


def bnb_request(tail):
    headers, data = create_data(tail)
    r = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data)
    # with open('/Users/dippmac/My_code/arbitrageAPI/bnc.json', 'w') as j:
    #     print(r.text, file=j)  # записываем строку в файл

    mys = json.loads(r.text)
    result = {}
    for bid in mys["data"][0:3]:
        price = bid["adv"]["price"]
        seller = bid["advertiser"]["nickName"]
        pay_method = bid["adv"]["tradeMethods"][0]["payType"]
        result[seller] = f"{price}({pay_method})"
        # result[seller] = float(price)

    # print(len(mys["data"]))
    # print('result: ', mys["data"][0]["adv"]["price"])
    # print('nickname: ', mys["data"][0]["advertiser"]["nickName"])

    # print(result)
    return result



