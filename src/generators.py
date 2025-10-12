from typing import Any, Generator


def filter_by_currency(data: list[dict], currency: str) -> Generator:
    """
    Фильтрация транзакций по заданной валюте
    """
    if data == []:
        return []
    else:
        for item in data:
            if item['operationAmount']['currency']['code'] == currency:
                yield item


def transaction_descriptions(data: list[dict]) -> Generator:
    """
    Функция вывода информации о назначении платежа по транзакции
    """
    if data == []:
        return []
    else:
        for item in data:
            yield item['description']


def card_number_generator(start_number: int, end_number: int) -> Generator:
    """
    Функция генерации номеров банковских карт
    """
    for item in range(start_number, end_number + 1):
        number_card = "0" * (16 - len(str(item))) + str(item)
        yield number_card[0:4] + " " + number_card[4:8] + " " + number_card[8:12] + " " + number_card[12:]
