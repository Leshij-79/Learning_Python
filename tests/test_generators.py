import pytest

from src.generators import (card_number_generator, filter_by_currency, filter_by_currency_csv_excel,
                            transaction_descriptions)


@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
        ),
        ("RUR", []),
    ],
)
def test_filter_by_currency(fixture_test_generator_transactions: list, currency: str, expected: list) -> None:
    """
    Тестирование функции фильтрации транзакций по заданной валюте файла json
    """
    filter_generator = list(filter_by_currency(fixture_test_generator_transactions, currency))
    assert filter_generator == expected

    filter_generator_second = list(filter_by_currency([], currency))
    assert filter_generator_second == [[]]


@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "amount": "9824.07",
                    "currency_name": "USD",
                    "currency_code": "USD",
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "amount": "79114.93",
                    "currency_name": "USD",
                    "currency_code": "USD",
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
        ),
        ("RUR", []),
    ],
)
def test_filter_by_currency_csv_excel(
    fixture_test_generator_transactions_csv_excel: list, currency: str, expected: list
) -> None:
    """
    Тестирование функции фильтрации транзакций по заданной валюте файла csv и excel
    """

    filter_generator = list(filter_by_currency_csv_excel(fixture_test_generator_transactions_csv_excel, currency))
    assert filter_generator == expected

    filter_generator_second = list(filter_by_currency_csv_excel([], currency))
    assert filter_generator_second == [[]]


@pytest.mark.parametrize("index, expected", [(0, "Перевод организации"), (1, "Перевод со счета на счет")])
def test_transaction_descriptions(fixture_test_generator_transactions: list, index: int, expected: str) -> None:
    generator_transaction_descriptions = list(transaction_descriptions(fixture_test_generator_transactions))
    assert generator_transaction_descriptions[index] == expected


def test_transaction_descriptions_none() -> None:
    generator_transaction_descriptions = list(transaction_descriptions([]))
    assert generator_transaction_descriptions == [[]]


@pytest.mark.parametrize(
    "index, expected",
    [(0, "1234 5678 9012 3456"), (1, "1234 5678 9012 3457"), (2, "1234 5678 9012 3458"), (3, "1234 5678 9012 3459")],
)
def test_card_number_generator(index: int, expected: str) -> None:
    """
    Тестирование генератора номеров банковских карт
    """
    start_number = 1234567890123456
    end_number = 1234567890123459
    start_card_number_generator = list(card_number_generator(start_number, end_number))
    assert start_card_number_generator[index] == expected
