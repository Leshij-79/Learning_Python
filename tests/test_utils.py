import json
from unittest.mock import Mock, patch

from src.utils import json_file_processing


@patch('json.load')
def test_json_file_processing(mock_json_file) -> None:
    mock_json = Mock()
    data_mock_for_test = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]
    mock_json.return_value.json.return_value = data_mock_for_test
    result = json_file_processing(mock_json)
    assert result == data_mock_for_test
