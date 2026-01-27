import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


def get_amount_in_rubles(transaction: dict) -> float:
    """Функция принимает на вход словарь с данными о транзакции.
    Возвращает сумму транзакции в Рублях.
    Если транзакция в иной валюте, то происходит обращение
    к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли"""
    try:
        currency = transaction["operationAmount"]["currency"]["code"]
        amount = float(transaction["operationAmount"]["amount"])

        if currency == "RUB":
            return amount

        url = "https://api.apilayer.com/exchangerates_data/convert" f"?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": API_KEY}

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise requests.exceptions.RequestException(f"Ошибка API: {response.status_code}")

        return round(float(response.json()["result"]), 2)

    except KeyError as error:
        raise KeyError(f"Ключ не найден: {error}")
