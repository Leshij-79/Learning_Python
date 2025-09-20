def get_mask_card_number(card_number: str) -> str:
    """Создание маски номера карты в формате ХХХХ ХХ** **** ХХХХ"""

    return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[12:]


def get_mask_account(account_number: str) -> str:
    """Создание маски номера счёта в формате **ХХХХ"""

    return "**" + account_number[16:]
