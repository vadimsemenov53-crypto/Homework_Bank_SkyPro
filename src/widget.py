import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str | None = None) -> str:
    """Функция возвращает строку с замаскированным номером карты или счет"""
    if not account_card:
        return "Информация о счете отсутствует"

    account = ""
    pattern = "Счет"

    if re.search(pattern, account_card):
        for element in account_card:
            if element.isdigit():
                account += element

        return "Счет " + get_mask_account(account)

    else:
        names_card = ""
        for element in account_card:
            if element.isdigit():
                account += element
            elif not element.isdigit():
                names_card += element

        if len(account) == 0:
            return names_card + " Номер карты отсутствует"
        else:
            return names_card + get_mask_card_number(account)


def get_date(date: str) -> str:
    """Функция возвращает дату из принятой строки
    (Формат строки -> "2024-03-11T02:26:18.671407")"""
    if not date or len(date) < 10:
        return "Информация о дате отсутствует"

    if not (date[0:4].isdigit() and date[5:7].isdigit() and date[8:10].isdigit()):
        return "Информация о дате отсутствует"

    return date[8:10] + "." + date[5:7] + "." + date[:4]
