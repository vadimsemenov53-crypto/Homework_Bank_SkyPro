import re
from collections import Counter

def filter_operations_by_description(data_operations: list[dict], search:str) -> list[dict]:
    """Функция принимает данные о банковских операциях (список словарей),
    возвращает список словарей у которых есть в описании переданная строка поиска."""
    pattern = re.compile(search, re.IGNORECASE)

    result_filter = []
    for operation in data_operations:
        if search:
            if pattern.findall(operation.get('description')):
                result_filter.append(operation)

        else:
            return []

    return result_filter


def count_operations_by_category(data_operations: list[dict], categories: list[str]) -> dict:
    """Функция принимает данные об операциях и список категория,
    возвращает словарь {название категорий -> количество операций}"""
    counter = Counter()

    for operation in data_operations:
        description = operation['description']

        if description in categories:
            counter[description] += 1

    return dict(counter)
