from typing import Any
from unittest.mock import Mock, patch

from src.external_api import transaction_processing


@patch("requests.get")
def test_transaction_processing(mock_requests_get) -> Any:
    """Тестирование API-запроса"""
    mock_requests = Mock()
    mock_requests.status_code = 200
    mock_requests.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1761493575, "rate": 79.61906},
        "date": "2025-10-26",
        "result": 654577.751312,
    }

    mock_requests_get.return_value = mock_requests

    test_data_usd = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }

    assert transaction_processing(test_data_usd) == 654577.75


@patch("requests.get")
def test_transaction_processing_bad_status_code(mock_requests_get) -> Any:
    """Тестирование API-запроса"""
    mock_requests = Mock()
    mock_requests.status_code = 403
    mock_requests.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1761493575, "rate": 79.61906},
        "date": "2025-10-26",
        "result": 654577.751312,
    }

    mock_requests_get.return_value = mock_requests

    test_data_usd = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }

    assert transaction_processing(test_data_usd) == 0.00


def test_transaction_processing_rub() -> Any:
    """Тестирование API-запроса"""
    test_data_rub = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }

    assert transaction_processing(test_data_rub) == 8221.37
