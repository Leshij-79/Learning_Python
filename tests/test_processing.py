import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import (fixture_test_filter_by_state, fixture_test_filter_by_date_first,
                            fixture_test_filter_by_date_second)


@pytest.mark.parametrize("test_name_state, expected", [
    ('EXECUTED', [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]),
    ('CANCELED', [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ])
])
def test_filter_by_state_first(fixture_test_filter_by_state: list, test_name_state: str, expected: list):
    assert filter_by_state(fixture_test_filter_by_state, test_name_state) == expected


@pytest.mark.parametrize("test_name_state, expected", [
    ('EXECUTED', 'Нет данных'),
    ('CANCELED', 'Нет данных')
])
def test_filter_by_state_second(test_name_state: str, expected: list):
    assert filter_by_state([], test_name_state) == expected


@pytest.mark.parametrize("test_reverse, expected_date", [
    (True, [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]),
    (False, [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ])
])
def test_sort_by_date_first(fixture_test_filter_by_date_first: list, test_reverse: bool, expected_date: list):
    assert sort_by_date(fixture_test_filter_by_date_first, test_reverse) == expected_date


@pytest.mark.parametrize("test_reverse, expected_date", [
    (True, [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-06-30T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T08:21:33.419441'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]),
    (False, [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-06-30T21:27:25.241689'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ])
])
def test_sort_by_date_first_second(fixture_test_filter_by_date_second: list, test_reverse: bool, expected_date: list):
    assert sort_by_date(fixture_test_filter_by_date_second, test_reverse) == expected_date


@pytest.mark.parametrize("list_by_filter, test_reverse, expected_date", [
    ([
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '30-06-2018T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ], True, [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '30-06-2018T02:08:58.425572'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
    ]),
    ([
        {'id': 939719570, 'state': 'EXECUTED', 'date': '30-06-2018T02:08:58.425572'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ], False, [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '30-06-2018T02:08:58.425572'}
    ])
])
def test_sort_by_date_first_third(list_by_filter: list, test_reverse: bool, expected_date: list):
    assert sort_by_date(list_by_filter, test_reverse) == expected_date

