def filter_by_state(bank_operaion: list, name_state: str = 'EXECUTED') -> list:
    """ """
    filtered_data = []

    for data in bank_operaion:
        if data['state'] == name_state:
            filtered_data.append(data)

    return filtered_data