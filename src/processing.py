def filter_by_state(bank_operaion: list, name_state: str = "EXECUTED") -> list:
    """Функция по фильтрации банковских операций по статусу"""
    if len(bank_operaion) == 0:
        return 'Нет данных'


    filtered_data = []

    for data in bank_operaion:
        if data["state"] == name_state:
            filtered_data.append(data)

    return filtered_data


def sort_by_date(bank_operation: list, reverce_direcion: bool = True) -> list:
    """Функция сортировки банковских операций по дате"""

    sorted_data = sorted(bank_operation, key=lambda data: data["date"], reverse=reverce_direcion)

    return sorted_data
