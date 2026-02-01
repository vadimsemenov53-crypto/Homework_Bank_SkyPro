import logging
import os

logs_path = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(logs_path, exist_ok=True)  # создаем папку автоматически, если она есть не падаем в ошибку

log_file_path = os.path.join(logs_path, "masks.log")

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file_path, mode="w")  # перезапись логера при каждом пуске
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

if not logger.handlers:  # исключаем дублирование хендлеров
    logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты клиента"""
    if not isinstance(card_number, str):
        logger.error(f"Произошла ошибка: {TypeError}")
        raise TypeError("Номер карты не является строкой")

    logger.info(f"Маскируем переданный номер карты: {card_number}")
    card_mask = card_number[:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[12:]

    logger.info("Выполняем проверку соответствия номера карты требованиям")
    if len(card_number) < 16:
        logger.error(f"Переданный номер содержит: {len(card_number)} символов < 16")
        return "Номер карты должен содержать 16 цифр"

    elif len(card_number) > 16:
        logger.error(f"Переданный номер содержит: {len(card_number)} символов > 16")
        return "Номер карты содержит более 16 цифр"

    else:
        logger.info("Успешная маскировка. Работа закончена.")
        return card_mask


def get_mask_account(numbers_account: str) -> str:
    """Функция маскирует номер счета"""
    if not isinstance(numbers_account, str):
        logger.error(f"Произошла ошибка: {TypeError}")
        raise TypeError("Номер счета не является строкой")

    logger.info(f"Принимаем для маскировки номер счета: {numbers_account}")
    mask_account = "**" + numbers_account[-4:]

    logger.info("Успешная маскировка. Работа закончена.")
    return mask_account
