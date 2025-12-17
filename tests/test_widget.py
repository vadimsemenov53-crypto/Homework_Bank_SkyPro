import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Счет 141421", "Счет **1421"),
        ("Visa Platinum 1212121212121212", "Visa Platinum 1212 12** **** 1212"),
        ("Мир 1212121212127777", "Мир 1212 12** **** 7777"),
    ],
)
def test_mask_account_card_base(account_card, expected):
    assert mask_account_card(account_card) == expected


def test_mask_account_card_invalid():
    assert mask_account_card("") == "Информация о счете отсутствует"
    assert mask_account_card() == "Информация о счете отсутствует"


def test_mask_account_card_none():
    assert mask_account_card(None) == "Информация о счете отсутствует"


def test_mask_account_card_fixture(widget_account_number, widget_card_number):
    assert mask_account_card(widget_account_number) == "Счет **2717"
    assert mask_account_card(widget_card_number) == "Visa Gold 1212 12** **** 1212"


def test_mask_account_card_wrong_type():
    with pytest.raises(TypeError):
        mask_account_card(312341)
    with pytest.raises(TypeError):
        mask_account_card(True)


def test_mask_account_card_no_digits():
    assert mask_account_card("Visa Platinum") == "Visa Platinum Номер карты отсутствует"


def test_get_date_basic(widget_get_date_base):
    assert get_date(widget_get_date_base) == "11.03.2024"


@pytest.mark.parametrize(
    "date, expected",
    [
        ("1999-12-01T23:59:59.000000", "01.12.1999"),
        ("2007-01-12T00:50:30.123456", "12.01.2007"),
        ("2022-11-30T12:30:20.663358", "30.11.2022"),
    ],
)
def test_get_date_another_date(date, expected):
    assert get_date(date) == expected


def test_get_date_non_string_input():
    with pytest.raises(TypeError):
        get_date(12345)
    with pytest.raises(TypeError):
        get_date()


def test_get_date_invalid():
    assert get_date("") == "Информация о дате отсутствует"


def test_get_date_invalid_format_not_empty():
    assert get_date("abc") == "Информация о дате отсутствует"


def test_get_date_invalid_but_long():
    assert get_date("abcd-ef-ghT00:00") == "Информация о дате отсутствует"
