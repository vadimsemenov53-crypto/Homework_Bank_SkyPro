from typing import Iterator


def filter_by_currency(transaction_data: list[dict], currency: str) -> Iterator[dict]:
    """Функция принимает на вход список словарей, представляющих транзакции.
    Поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)."""
    for index in range(len(transaction_data)):
        if transaction_data[index]["operationAmount"]['currency']['code'] == currency.upper():
            yield transaction_data[index]
