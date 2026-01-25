import requests
from dotenv import load_dotenv

def get_amount_in_rubles(transaction: dict) -> float:
    """Функция принимает на вход словарь с данными о транзакции.
    Возвращает сумму транзакции в Рублях.
    Если транзакция в иной валюте, то происходит обращение
    к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли"""
    pass



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