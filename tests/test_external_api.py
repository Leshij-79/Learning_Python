from unittest.mock import Mock, patch

from src.external_api import transaction_processing


@patch('requests.get')
def test_transaction_processing(mock_get) -> None:
    mock_get.return_value.json.return_value = {
        'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37},
        'info': {'timestamp': 1761493575, 'rate': 79.61906}, 'date': '2025-10-26',
        'result': 654577.751312
    }
    test_data_usd = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }
    result = transaction_processing(test_data_usd)
    assert result == 654577.75
