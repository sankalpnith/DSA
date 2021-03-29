#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'calculateHoldingValue' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts STRING date (in yyyymmdd format) as parameter.
#
import json
from urllib import request


def get_request(url):
    return json.loads(request.urlopen(url).read().decode())


def calculateHoldingValue(date):
    paging_holding_request = get_request("https://api.myjson.com/bins/10ysxg")
    holding_dict = {}
    found_holding = False
    paging_price_request = get_request("https://api.myjson.com/bins/6ycbo")
    total_value = 0
    found_price = False
    while (paging_holding_request.get('data')):
        data = paging_holding_request.get('data')
        price_data = paging_price_request.get('data')
        if int(data[-1].get('date')) >= int(date) and int(data[0].get('date')) <= int(date):
            for record in data:
                if record.get('date') == date:
                    found_holding = True
                    holding = {
                        record.pop('security'): record
                    }
                    holding_dict.update(holding)
                elif found_holding:
                    break
        elif found_holding:
            break
        if paging_holding_request.get('nextPage'):
            paging_holding_request = get_request(paging_holding_request.get('nextPage'))
        else:
            paging_holding_request = {}

    # ===========================
    paging_price_request = get_request("https://api.myjson.com/bins/6ycbo")
    total_value = 0
    found_price = False
    while (paging_price_request.get('data')):
        data = paging_price_request.get('data')
        if int(data[-1].get('date')) >= int(date) and int(data[0].get('date')) <= int(date):
            for record in data:
                if record.get('date') == date:
                    found_price = True
                    holding_dict[record.get('security')]['price'] = record.get('price')
                    total_value += record.get('price') * holding_dict.get(record.get('security'), {}).get('quantity')
                elif found_price:
                    break
        elif found_price:
            break
        if paging_price_request.get('nextPage'):
            paging_price_request = get_request(paging_price_request.get('nextPage'))
        else:
            paging_holding_request = {}

    return total_value




