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


def card_number_generator(start_gen: int, stop_gen: int) -> Generator[str]:
    """Генератор, который выдает номера банковских карт в формате
     ( XXXX XXXX XXXX XXXX ), где X — цифра номера карты.
     Генератор может сгенерировать номера карт в заданном диапазоне
      от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    if start_gen > stop_gen:
        yield f'Заданы неверные параметры start > stop: {start_gen} > {stop_gen}'
    else:
        for num in range(start_gen, stop_gen+1):
            if num < 10000000000000000:
                card_number = str(num).zfill(16)
                yield f'{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}'
            else:
                yield 'Достигнуто крайнее значение: 9999 9999 9999 9999'
