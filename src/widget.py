import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция возвращает строку с замаскированным номером карты или счет"""
    account = ""
    pattern = "Счет"

    if re.search(pattern, account_card):
        for element in account_card:
            if element.isdigit():
                account += element

        return "Счет " + get_mask_account(account)

    elif not re.search(pattern, account_card):
        names_card = ""
        for element in account_card:
            if element.isdigit():
                account += element
            elif not element.isdigit():
                names_card += element

        return names_card + get_mask_card_number(account)

    else:
        return "Информация о счете отсутствует"


def get_date(date: str) -> str:
    """Функция возвращает дату из принятой строки
    (Формат строки -> "2024-03-11T02:26:18.671407")"""
    return date[8:10] + "." + date[5:7] + "." + date[:4] + " (ДД.ММ.ГГГГ)"
