from src.masks import get_mask_account, get_mask_card_number

help(get_mask_card_number)
card_number = str(input("Введите номер карты (16 цифр): "))
print(get_mask_card_number(card_number))

help(get_mask_account)
number_account = str(input("Введите номер лицевого счета:"))
print(get_mask_account(number_account))
