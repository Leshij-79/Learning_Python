import re

from dateutil.parser import parse

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(information_account_card: str) -> str:
    """
    Обработка данных счёта или карты
    """
    if "Сч" in information_account_card or "сч" in information_account_card:
        temp_account_number = ""

        for symbol in re.findall(r"[0-9]+", information_account_card):
            temp_account_number += symbol

        string_mask_account = get_mask_account(temp_account_number)

        if "ве" not in string_mask_account:
            return information_account_card[:-20] + string_mask_account
        else:
            return string_mask_account
    else:
        temp_card_number = ""

        for symbol in re.findall(r"[0-9]+", information_account_card):
            temp_card_number += symbol

        string_mask_card = get_mask_card_number(temp_card_number)

        if "ве" not in string_mask_card:
            return information_account_card[:-16] + string_mask_card
        else:
            return string_mask_card


def get_date(information_date: str) -> str:
    """Обработка строки содержащую дату"""

    try:
        parse(information_date[0:10])

    except ValueError:
        return "Дата не введена"

    if information_date[2:3].isnumeric():
        return information_date[8:10] + "." + information_date[5:7] + "." + information_date[0:4]
    else:
        return information_date[0:2] + "." + information_date[3:5] + "." + information_date[6:10]
