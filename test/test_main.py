from src.widget import get_date, mask_account_card

help(mask_account_card)
print(mask_account_card("Счет 13312445665"))
print(mask_account_card("Visa Platinum 2342342345878799"))
print(mask_account_card("Maestro 1596837868705199"))
print("")

help(get_date)
print(get_date("2024-03-11T02:26:18.671407"))
print(get_date("2021-12-25T03:29:11.883052"))
