def get_mask_card_number(card_number: str) -> str:
    """Создание маски номера карты в формате ХХХХ ХХ** **** ХХХХ"""

    if len(card_number) == 0:
        return "Номер карты не введен"

    if (not card_number.isdigit() or len(card_number) != 16):
        return "Не верный номер карты"



    return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[12:]


def get_mask_account(account_number: str) -> str:
    """Создание маски номера счёта в формате **ХХХХ"""

    if len(account_number) == 0:
        return "Номер счёта не введен"

    if (not account_number.isdigit() or len(account_number) != 20):
        return "Не верный номер счёта"

    return "**" + account_number[16:]
