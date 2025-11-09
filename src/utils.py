import csv
import json
import logging
import os
from typing import Any

import pandas as pd

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
        logger.critical("Файл json не найден")
        return []

    if len(data) == 0 or type(data) is not list:
        logger.error("Нет данных или не верный формат данных")
        return []
    else:
        logger.info("Получены данные по транзакциям из json-файла")
        return data


def read_transaction_csv(file_name: str, delimiter: str = ",") -> list[dict]:
    """
    Функция чтения данных по транзакциям из csv-файла
    :param file_name: Путь к csv-файлу в формате str
    :param delimiter: Принимает разделитель данных в csv-файле в формате str. По-умолчанию ','
    :return: Список словарей list[dict]
    """
    try:
        with open(file_name, "r", encoding="utf-8") as csv_file:
            reader = list(csv.DictReader(csv_file, delimiter=delimiter))
            logger.info("Данные с csv-файла прочитаны")

    except FileNotFoundError:
        logger.critical("Файл csv не найден")
        return []

    return reader


def read_transaction_excel(file_name: str) -> list[dict[Any, Any]]:
    """
    Функция чтения данных транзакций из xlsx-файла
    :param file_name: путь к xlsx-файлу в формате str
    :return: список словарей list[dict]
    """
    try:
        excel_data = pd.read_excel(file_name)
        logger.info("Данные с xlsx-файла прочитаны")
        return excel_data.to_dict("records")
    except FileNotFoundError:
        logger.critical("XLSX-файл не найден")
        return []


print(read_transaction_excel("../data/transactions_excel.xlsx"))
