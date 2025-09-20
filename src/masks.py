def mask_account_card(information_account_card: str) -> str:
    """Обработка данных счёта или карты"""

    if information_account_card[-20:-19].isnumeric():
        return information_account_card[:-20] + get_mask_account(information_account_card[-20:])
    else:
        return information_account_card[:-16] + get_mask_card_number(information_account_card[-16:])


def get_mask_card_number(card_number: str) -> str:
    """Создание маски номера карты в формате ХХХХ ХХ** **** ХХХХ"""

    return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[12:]


def get_mask_account(account_number: str) -> str:
    """Создание маски номера счёта в формате **ХХХХ"""

    return "**" + account_number[16:]
