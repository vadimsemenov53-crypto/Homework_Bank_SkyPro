def filter_by_state(data_list: list, state: str = "EXECUTED") -> list:
    """Функция фильтрует полученные данные по ключу state
    (по умолчанию state='EXECUTED')"""
    filtered_list = []

    for info in data_list:
        if info.get('state', '') == state:
            filtered_list.append(info)

    return filtered_list


def sort_by_date(data_list: list, sort: bool = True) -> list:
    """Функция сортирует полученные данные по дате
    принимая список словарей и параметр сортировки,
    возвращает отсортированный список словарей.
    Сортировка по умолчанию - убывание (sort = True)"""
    if sort:
        sorted_list = sorted(data_list, key=lambda info: info["date"][:10], reverse=True)
        return sorted_list
    else:
        sorted_list = sorted(data_list, key=lambda info: info["date"][:10], reverse=False)
        return sorted_list
