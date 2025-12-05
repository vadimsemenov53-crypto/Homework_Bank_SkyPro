import pytest

from src.widget import mask_account_card, get_date

def test_mask_account_card_base():
    assert mask_account_card('Счет 141421') == 'Счет **1421'
    assert mask_account_card('Visa Platinum 1212121212121212') == 'Visa Platinum 1212 12** **** 1212'


def test_mask_account_card_invalid():
    assert mask_account_card('') == 'Информация о счете отсутствует'
    assert mask_account_card() == 'Информация о счете отсутствует'