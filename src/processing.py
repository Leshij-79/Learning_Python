import re
from collections import Counter


def filter_by_state(bank_operaion: list, name_state: str = "EXECUTED") -> list:
    """
    Функция по фильтрации банковских операций по статусу
    """
    if len(bank_operaion) == 0:
        return []

    filtered_data = []

    for data in bank_operaion:

        if len(data) == 0:
            continue

        if data["state"] == name_state:
            filtered_data.append(data)

    return filtered_data


def sort_by_date(bank_operation: list, reverce_direcion: bool = True) -> list:
    """
    Функция сортировки банковских операций по дате
    """
    sorted_data = sorted(bank_operation, key=lambda data: data["date"], reverse=reverce_direcion)

    return sorted_data


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция поиска данных в списке банковских операций в описании операции
    :param data: Список словарей с данными о банковских операциях
    :param search: Строка поиска
    :return: Список словарей банковских операций, у которых в описании есть данная строка
    """
    processed_data = []

    for item in data:
        result = re.search(search, item["description"], flags=re.IGNORECASE)
        if result is None:
            continue
        processed_data.append(item)

    return processed_data


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Функция подсчёта количества операций по заданным категориям
    :param data: Список словарей с данными о банковских операциях
    :param categories: Список категорий операций
    :return: Словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории
    """
    processed_data = []

    for item in data:
        if item["description"] in categories:
            processed_data.append(item["description"])

    processed_description = dict(Counter(processed_data))

    print(type(processed_description))

    return processed_description
