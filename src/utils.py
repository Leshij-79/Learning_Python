import json


def json_file_processing(file_name: str) -> list:
    """
    Функция получения данных по транзакциям из json-файла
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        return []


    if len(data) == 0 or type(data) != list:
        return []
    else:
        return data
