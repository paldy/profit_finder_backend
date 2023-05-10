import os
import requests
import xml.etree.ElementTree as ET


def parsing_data(currency, xml):
    root = ET.fromstring(xml)
    result = ''
    for child in root:
        for x in child:
            if x.tag == 'CharCode' and x.text == currency:
                result = child.find('Value').text

    return result


# https://www.cbr.ru/development/SXML/
def sbr_request(input_data):
    r = requests.post('https://www.cbr.ru/scripts/XML_daily.asp')
    # with open(os.path.dirname(__file__) + 'sbr.xml', 'w') as j:
    #     print(r.text, file=j)  # записываем строку в файл

    result = parsing_data(input_data.asset, r.text)

    return result


# print(sbr_request('USD'))


