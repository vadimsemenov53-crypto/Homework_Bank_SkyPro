import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_base(card_number):
    assert get_mask_card_number(card_number) == "2202 00** **** 4707"


@pytest.mark.parametrize(
    "cards_numbers, expected",
    [
        ("2343254543423654", "2343 25** **** 3654"),
        ("2717254543427777", "2717 25** **** 7777"),
        ("5555254543421212", "5555 25** **** 1212"),
    ],
)
def test_get_mask_card_number_base_full(cards_numbers, expected):
    assert get_mask_card_number(cards_numbers) == expected


@pytest.mark.parametrize(
    "card_number_wrong, expected",
    [
        ("234325454342365400", "Номер карты содержит более 16 цифр"),
        ("271725454342777", "Номер карты должен содержать 16 цифр"),
        ("", "Номер карты должен содержать 16 цифр"),
    ],
)
def test_get_mask_card_number_wrong(card_number_wrong, expected):
    assert get_mask_card_number(card_number_wrong) == expected


def test_get_mask_card_number_wrong_type():
    with pytest.raises(TypeError):
        get_mask_card_number(1234567890123456)


def test_get_mask_card_number():
    with pytest.raises(TypeError):
        get_mask_card_number()


def test_get_mask_account(number_account):
    assert get_mask_account(number_account) == "**1201"


@pytest.mark.parametrize(
    "numbers_accounts, expected", [("23084028", "**4028"), ("5678323525", "**3525"), ("154627854400", "**4400")]
)
def test_get_mask_account_full(numbers_accounts, expected):
    assert get_mask_account(numbers_accounts) == expected


def test_get_mask_account_wrong_type():
    with pytest.raises(TypeError):
        get_mask_account(245789908754)
