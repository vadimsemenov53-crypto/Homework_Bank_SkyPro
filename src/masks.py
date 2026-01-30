import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/masks.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты клиента"""
    logger.info(f"Маскируем переданный номер карты: {card_number}")
    card_mask = card_number[:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[12:]

    logger.info(f"Выполняем проверку соответствия номера карты требованиям")
    if len(card_number) < 16:
        logger.warning(f"Переданный номер содержит: {len(card_number)} символов < 16")
        return "Номер карты должен содержать 16 цифр"
    elif len(card_number) > 16:
        logger.warning(f'Переданный номер содержит: {len(card_number)} символов > 16')
        return "Номер карты содержит более 16 цифр"
    else:
        logger.info('Успешная маскировка. Работа закончена.')
        return card_mask


def get_mask_account(numbers_account: str) -> str:
    """Функция маскирует номер счета"""
    mask_account = "**" + numbers_account[-4:]
    return mask_account
