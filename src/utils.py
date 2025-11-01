import json
import logging
import os

path_log_directory = os.path.join(os.path.dirname(__file__), "../logs", "utils.log")
logger = logging.getLogger(__name__) if __name__ != "__main__" else logging.getLogger("src.utils")
file_handler = logging.FileHandler(path_log_directory, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def json_file_processing(file_name: str) -> list:
    """
    Функция получения данных по транзакциям из json-файла
    """
    try:
        with open(file_name, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        logger.critical("Файл не найден")
        return []

    if len(data) == 0 or type(data) is not list:
        logger.error("Нет данных или не верный формат данных")
        return []
    else:
        logger.info("Получены данные по транзакциям из json-файла")
        return data
