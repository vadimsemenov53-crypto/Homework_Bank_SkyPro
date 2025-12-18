from typing import Generator


def filter_by_currency(transaction_data: list[dict], currency: str) -> Generator[dict]:
    """Функция принимает на вход список словарей, представляющих транзакции.
    Поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)."""
    for index in range(len(transaction_data)):
        if transaction_data[index]["operationAmount"]['currency']['code'] == currency.upper():
            yield transaction_data[index]


def transaction_descriptions(transaction_data: list[dict]) -> Generator[str]:
    """Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    if transaction_data:
        for data in transaction_data:
            yield data["description"]
    else:
        yield 'Нет данных'