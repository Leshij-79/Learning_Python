import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize('test_information_account_card, expected', [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Счет 35383033474447895560', 'Счет **5560'),
    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
    ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
    ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
    ('Счет 73654108430135874305', 'Счет **4305'),
    ('Visa Gold 599941422842653', 'Visa Gold Не верный номер карты')
])
def test_mask_account_card(test_information_account_card: str, expected: str):
    assert mask_account_card(test_information_account_card) == expected


@pytest.mark.parametrize('test_information_date,expected',[
    ('2024-03-11T02:26:18.671407','11.03.2024'),
    ('2025-10-01T02:26:18.671407','01.10.2025'),
    ('2025-10-0T02:26:18.671407', 'Дата не введена'),
    ('01-10-2025T02:26:18.671407','01.10.2025'),
    ('01/10/2025T02:26:18.671407','01.10.2025'),
    ('2024/03/11T02:26:18.671407', '11.03.2024'),
    ('2025-10-001T02:26:18.671407','Дата не введена')
])
def test_get_date(test_information_date: str, expected: str):
    assert get_date(test_information_date) == expected
