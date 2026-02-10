import re

def filter_operations_by_description(data_operations: list[dict], search:str) -> list[dict]:
    """Функция принимает данные о банковских операциях (список словарей),
    возвращает список словарей у которых есть в описании переданная строка поиска."""
    pattern = re.compile(search, re.IGNORECASE)

    result_filter = []
    for operations in data_operations:
        if search:
            if pattern.findall(operations.get('description')):
                result_filter.append(operations)

        else:
            return []

    return result_filter

