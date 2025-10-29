import json

import requests
from dotenv import load_dotenv
import os


def transaction_processing(transaction: dict) -> float:
    """
    Функция обработки транзакции - конвертация суммы операции в российские рубли
    """
    if transaction['operationAmount']['currency']['code'] == 'RUB':
        return float(transaction['operationAmount']['amount'])
    elif (transaction['operationAmount']['currency']['code'] == 'USD'
          or transaction['operationAmount']['currency']['code'] == 'EUR'):
        load_dotenv()
        api_key = os.getenv('API_KEY')
        to_ = 'RUB'
        from_ = transaction['operationAmount']['currency']['code']
        amount_ = transaction['operationAmount']['amount']
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_}&from={from_}&amount={amount_}"

        payload = {}
        headers = {
            'apikey':api_key
        }
        response = requests.get(url, headers=headers, data=payload)

        status_code = response.status_code
        if status_code == 200:
            result = response.json()
            # print(result)
#            result = json.loads(response.text)
        else:
            return 0.00

        return round(float(result['result']),2)


# data_rub = {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   }
#
# data_usd = {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   }
# data_eur = {
#     "id": 939719570,
#     "state": "EXECUTED",
#     "date": "2018-06-30T02:08:58.425572",
#     "operationAmount": {
#       "amount": "9824.07",
#       "currency": {
#         "name": "EUR",
#         "code": "EUR"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Счет 75106830613657916952",
#     "to": "Счет 11776614605963066702"
#   }
#
#print(transaction_processing(data_usd))
#transaction_processing(data_usd)