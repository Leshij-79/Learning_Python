from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(information_account_card: str) -> str:
    """Обработка данных счёта или карты"""

    if information_account_card[-20:-19].isnumeric():
        return information_account_card[:-20] + get_mask_account(information_account_card[-20:])
    else:
        return information_account_card[:-16] + get_mask_card_number(information_account_card[-16:])


def get_date(information_date: str) -> str:
    """Обработка строки содержащую дату"""

    return information_date[8:10] + "." + information_date[5:7] + "." + information_date[0:4]
