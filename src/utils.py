import json
from json import JSONDecodeError


def get_operations(path_to_file: str) -> list[dict]:
    """Функция принимает путь до файла: {path} (файл с расширением 'json') с банковскими операция
    и возвращает список словарей банковских операций.
    Пример пути ->
    '/Users/vadimsemenov/PycharmProjects/Homework_Bank_SkyPro/data/operations.json'"""

    try:
        with open(path_to_file, encoding="utf-8") as operations_file:
            try:
                data_operations = json.load(operations_file)
            except JSONDecodeError:
                return []
    except FileNotFoundError:
        return []

    if not isinstance(data_operations, list):
        return []

    if not data_operations:
        return []

    return data_operations
