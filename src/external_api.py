import os

import requests
from dotenv import load_dotenv


def transaction_processing(transaction: dict) -> float | None:
    """
    Функция обработки транзакции - конвертация суммы операции в российские рубли
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    elif (
        transaction["operationAmount"]["currency"]["code"] == "USD"
        or transaction["operationAmount"]["currency"]["code"] == "EUR"
    ):
        load_dotenv()
        api_key = os.getenv("API_KEY")
        to_ = "RUB"
        from_ = transaction["operationAmount"]["currency"]["code"]
        amount_ = transaction["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_}&from={from_}&amount={amount_}"
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)

        status_code = response.status_code
        if status_code == 200:
            result = response.json()
        else:
            return 0.00

        return round(float(result["result"]), 2)
