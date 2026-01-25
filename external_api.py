import requests
from dotenv import load_dotenv

load_dotenv('.env')

API_KEY =

def get_amount_in_rubles(transaction: dict) -> float:
    """Функция принимает на вход словарь с данными о транзакции.
    Возвращает сумму транзакции в Рублях.
    Если транзакция в иной валюте, то происходит обращение
    к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли"""
    try:
        if transaction['operationAmount']['currency']['code'] == 'RUB':
            return transaction['operationAmount']['amount']
        else:

    except KeyError:
        raise KeyError('Не найден ключ')
    return 0



transaction_data = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
print(get_amount_in_rubles(transaction_data))
