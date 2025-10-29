import json
from typing import Any
from unittest.mock import mock_open, patch

from src.utils import json_file_processing


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

@patch("builtins.open", new_callable=mock_open)
def test_json_file_processing_no_data(mock_json_file) -> Any:
    """Тестирование чтения json-файла без данных"""
    data_mock_for_test = []

    mock_file = mock_json_file.return_value
    mock_file.read.return_value = json.dumps(data_mock_for_test)

    assert json_file_processing('') == data_mock_for_test
