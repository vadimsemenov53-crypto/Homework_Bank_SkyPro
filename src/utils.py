import json
import logging
import os
from json import JSONDecodeError

logs_path = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(logs_path, exist_ok=True)  # создаем папку автоматически, если она есть не падаем в ошибку

log_file_path = os.path.join(logs_path, "utils.log")

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file_path, mode="w")  # перезапись логера при каждом пуске
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

if not logger.handlers:  # исключаем дублирование хендлеров
    logger.addHandler(file_handler)


def get_operations(path_to_file: str) -> list[dict]:
    """Функция принимает путь до файла: {path} (файл с расширением 'json') с банковскими операция
    и возвращает список словарей банковских операций.
    Пример пути ->
    '/Users/vadimsemenov/PycharmProjects/Homework_Bank_SkyPro/data/operations.json'"""

    try:
        logger.info(f'Открываем переданный файл: {path_to_file}')
        with open(path_to_file, encoding="utf-8") as operations_file:
            try:
                logger.info("Декодируем переданные данные")
                data_operations = json.load(operations_file)
            except JSONDecodeError:
                logger.error("Ошибка в JSON-файле.")
                return []
    except FileNotFoundError:
        logger.error("Файл не найден.")
        return []

    if not isinstance(data_operations, list):
        logger.error("Ожидался список операций.")
        return []

    if not data_operations:
        logger.error("Список пуст.")
        return []

    logger.info("Возвращаем полученный список банковских операций. Успешное завершение работы.")
    return data_operations
