import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "test_card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("6543210987654321", "6543 21** **** 4321"),
        ("234567890123456", "Не верный номер карты"),
        ("1234fff890123456", "Не верный номер карты"),
        ("1234 67890123456", "Не верный номер карты"),
        ("", "Номер карты не введен"),
    ],
)
def test_get_mask_card_number(test_card_number: str, expected: str) -> None:
    """
    Тест на маскировку номера карты
    """
    assert get_mask_card_number(test_card_number) == expected


@pytest.mark.parametrize(
    "test_account_number, expected",
    [
        ("12345678901234567890", "**7890"),
        ("09876543210987654321", "**4321"),
        ("2345678901234567890", "Не верный номер счёта"),
        ("1234fff8901234567890", "Не верный номер счёта"),
        ("1234 678901234567890", "Не верный номер счёта"),
        ("", "Номер счёта не введен"),
    ],
)
def test_get_mask_account(test_account_number: str, expected: str) -> None:
    """
    Тест на маскировку номера счёта
    """
    assert get_mask_account(test_account_number) == expected
