# def test_mask_account_card(information_account_card: str) -> str:
#     pass
#
#
import pytest

from src.widget import get_date


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
