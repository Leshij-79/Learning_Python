import json
from typing import Any
from unittest.mock import mock_open, patch, Mock

import pandas as pd


from src.utils import json_file_processing, read_transaction_csv, read_transaction_excel


@patch("builtins.open", new_callable=mock_open)
def test_json_file_processing(mock_json_file) -> Any:
    """Тестирование чтения json-файла"""
    data_mock_for_test = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]

    mock_file = mock_json_file.return_value
    mock_file.read.return_value = json.dumps(data_mock_for_test)

    assert json_file_processing('') == data_mock_for_test

def test_json_file_processing_error() -> Any:
    """Тестирование чтения json-файла при ошибочном имени"""

    assert json_file_processing('') == []

@patch("builtins.open", new_callable=mock_open)
def test_json_file_processing_no_data(mock_json_file) -> Any:
    """Тестирование чтения json-файла без данных"""
    data_mock_for_test = []

    mock_file = mock_json_file.return_value
    mock_file.read.return_value = json.dumps(data_mock_for_test)

    assert json_file_processing('') == data_mock_for_test

@patch("builtins.open", new_callable=mock_open, read_data='id;state;date;amount;currency_name;currency_code;from;'
                                                          'to;description\n650703;EXECUTED;2023-09-05T11:30:32Z;16210;'
                                                          'Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;'
                                                          'Перевод организации')
def test_read_transaction_csv(mock_csv_file) -> Any:
    """Тестирование csv-файла"""
    data_mock_for_test = [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210',
                           'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
                           'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'}]

    assert read_transaction_csv('',';') == data_mock_for_test

def test_read_transaction_csv_error() -> Any:
    """Тестирование csv-файла при ошибочном имени"""

    assert read_transaction_csv('') == []

@patch("pandas.read_excel")
def test_read_transaction_excel(mock_pd_read_excel) -> Any:
    """Тестирование xlsx-файла"""
    data_mock_for_test = [{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0,
                           'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
                           'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'}]
    mock_pd_read_excel.return_value = pd.DataFrame(data_mock_for_test)
    result = read_transaction_excel('')
    assert result == data_mock_for_test
