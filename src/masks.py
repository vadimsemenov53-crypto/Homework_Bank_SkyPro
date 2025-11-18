def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты клиента"""
    card_mask = card_number[:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[12:]

    if len(card_number) < 16:
        return "Номер карты должен содержать 16 цифр"
    elif len(card_number) > 16:
        return "Номер карты содержит более 16 цифр"
    else:
        return card_mask


def get_mask_account(numbers_account: str) -> str:
    """Функция маскирует номер счета"""
    mask_account = "**" + numbers_account[-4:]
    return mask_account
