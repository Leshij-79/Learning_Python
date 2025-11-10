import pytest

from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


@pytest.mark.parametrize(
    "test_name_state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state_first(fixture_test_filter_by_state: list, test_name_state: str, expected: list) -> None:
    """
    Первый тест по фильтации операций с изменением поля state
    """

    assert filter_by_state(fixture_test_filter_by_state, test_name_state) == expected


@pytest.mark.parametrize("test_name_state, expected", [("EXECUTED", []), ("CANCELED", [])])
def test_filter_by_state_second(test_name_state: str, expected: list) -> None:
    """
    Второй тест по фильтации операций с изменением поля state, а также отсутствующими данными
    """
    assert filter_by_state([], test_name_state) == expected


@pytest.mark.parametrize(
    "test_reverse, expected_date",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date_first(fixture_test_filter_by_date_first: list, test_reverse: bool, expected_date: list) -> None:
    """
    Первый тест сортировки списка операций по полю date
    """
    assert sort_by_date(fixture_test_filter_by_date_first, test_reverse) == expected_date


@pytest.mark.parametrize(
    "test_reverse, expected_date",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T08:21:33.419441"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T21:27:25.241689"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date_first_second(
    fixture_test_filter_by_date_second: list, test_reverse: bool, expected_date: list
) -> None:
    """
    Второй тест сортировки по полю date для проверки сортировки при одинаковых датах
    """

    assert sort_by_date(fixture_test_filter_by_date_second, test_reverse) == expected_date


@pytest.mark.parametrize(
    "list_by_filter, test_reverse, expected_date",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "30-06-2018T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            True,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "30-06-2018T02:08:58.425572"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
        ),
        (
            [
                {"id": 939719570, "state": "EXECUTED", "date": "30-06-2018T02:08:58.425572"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "30-06-2018T02:08:58.425572"},
            ],
        ),
    ],
)
def test_sort_by_date_first_third(list_by_filter: list, test_reverse: bool, expected_date: list) -> None:
    """
    Третий тест сортировки по полю date с целью проверки сортировки при разных форматах даты
    """
    assert sort_by_date(list_by_filter, test_reverse) == expected_date


@pytest.mark.parametrize("search", ["перевод"])
def test_process_bank_search(fixture_test_process_bank: list, search: str) -> None:
    """
    Тест функции поиска данных в списке банковских операций в описании операции
    :param fixture_test_process_bank: Список словарей банковских операций
    :param search: Строка поиска
    :return: None
    """
    result = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
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
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 214024827,
            "state": "EXECUTED",
            "date": "2018-12-20T16:43:26.929246",
            "operationAmount": {"amount": "70946.18", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 10848359769870775355",
            "to": "Счет 21969751544412966366",
        },
    ]

    assert process_bank_search(fixture_test_process_bank, search) == result


@pytest.mark.parametrize("categories", [("Перевод организации", "Перевод со счета на счет", "Открытие вклада")])
def test_process_bank_operations(fixture_test_process_bank: list, categories: list) -> None:
    """
    Тест функции подсчёта количества операций по заданным категориям
    :param fixture_test_process_bank: Список словарей банковских операций
    :param categories: Список категорий
    :return: None
    """
    result = {"Перевод организации": 4, "Открытие вклада": 1, "Перевод со счета на счет": 2}

    assert process_bank_operations(fixture_test_process_bank, categories) == result
