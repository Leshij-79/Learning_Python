import logging
import os

path_log_directory = os.path.join(os.path.dirname(__file__), "../logs", "masks.log")
logger = logging.getLogger(__name__) if __name__ != "__main__" else logging.getLogger("src.masks")
file_handler = logging.FileHandler(path_log_directory, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """
    Создание маски номера карты в формате ХХХХ ХХ** **** ХХХХ
    """
    if len(card_number) == 0:
        logger.error("Номер карты не введен")
        return "Номер карты не введен"

    if not card_number.isdigit() or len(card_number) != 16:
        logger.error("Не верный номер карты")
        return "Не верный номер карты"

    logger.info("Маска номера карты создана успешно")
    return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[12:]


def get_mask_account(account_number: str) -> str:
    """
    Создание маски номера счёта в формате **ХХХХ
    """
    if len(account_number) == 0:
        logger.error("Номер счёта не введен")
        return "Номер счёта не введен"

    if not account_number.isdigit() or len(account_number) != 20:
        logger.error("Не верный номер счёта")
        return "Не верный номер счёта"

    logger.info("Маска номера счёта содана успешно")
    return "**" + account_number[16:]
