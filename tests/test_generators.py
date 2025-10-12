import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(fixture_test_generator_transactions: list) -> None:
    """
    Тест функции генератора фильтрации данных по транзакциям
    """
    currency = "USD"
    ext1 = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    ext2 = {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    ext3 = {}  # mypy выдаёт ошибку
    filter_generator = filter_by_currency(fixture_test_generator_transactions, currency)
    filter_generator_rur = filter_by_currency(fixture_test_generator_transactions, "RUR")
    filter_generator_null = filter_by_currency([], currency)
    assert next(filter_generator) == ext1
    assert next(filter_generator) == ext2
    assert next(filter_generator_rur) == ext3
    assert next(filter_generator_null) == ext3


# @pytest.mark.parametrize("currency, expected", [
#      ("USD",[{"id": 939719570,"state": "EXECUTED","date": "2018-06-30T02:08:58.425572","operationAmount":
#                 {"amount": "9824.07","currency":
#                     {"name": "USD","code": "USD"}
#                  },
#               "description": "Перевод организации","from": "Счет 75106830613657916952",
#               "to": "Счет 11776614605963066702"}]),
#     ("USD",[{"id": 142264268,"state": "EXECUTED","date": "2019-04-04T23:20:05.206878","operationAmount":
#                 {"amount": "79114.93","currency":
#                     {"name": "USD", "code": "USD"}
#                  },
#               "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542",
#               "to": "Счет 75651667383060284188"}]),
#     ("RUR",[])
# ])
# def test_filter_by_currency(fixture_test_generator_transactions: list, currency: str, expected: list) -> None:
#
#     filter_generator = list(filter_by_currency(fixture_test_generator_transactions, currency))
#     assert filter_generator == expected


def test_transaction_descriptions(fixture_test_generator_transactions: list) -> None:
    """
    Тестирование функции генератора по выводу назначения платежа по транзакции
    """
    generator_transaction_descriptions = transaction_descriptions(fixture_test_generator_transactions)
    assert next(generator_transaction_descriptions) == "Перевод организации"
    assert next(generator_transaction_descriptions) == "Перевод со счета на счет"


# @pytest.mark.parametrize('expected',[(["Перевод организации"]), (["Перевод со счета на счет"])])
# def test_transaction_descriptions(fixture_test_generator_transactions: list, expected: str) -> None:
#     generator_transaction_descriptions = list(transaction_descriptions(fixture_test_generator_transactions))
#     assert generator_transaction_descriptions == expected


def test_card_number_generator() -> None:
    """
    Тестирование генератора номеров банковских карт
    """
    ext1 = "1234 5678 9012 3456"
    ext2 = "1234 5678 9012 3457"
    ext3 = "1234 5678 9012 3458"
    ext4 = "1234 5678 9012 3459"
    start_card_number_generator = card_number_generator(1234567890123456, 1234567890123459)
    assert next(start_card_number_generator) == ext1
    assert next(start_card_number_generator) == ext2
    assert next(start_card_number_generator) == ext3
    assert next(start_card_number_generator) == ext4
