def filter_by_state(data_list: list, state: str = "EXECUTED") -> list:
    """Функция фильтрует полученные данные по ключу state
    (по умолчанию state='EXECUTED')"""
    filtered_list = []

    for info in data_list:
        if info["state"] == state:
            filtered_list.append(info)

    return filtered_list
