import pytest


@pytest.fixture()
def card_number():
    return "2202001366664707"


@pytest.fixture()
def number_account():
    return "271728141201"


@pytest.fixture()
def widget_account_number():
    return 'Счет 474733892717'


@pytest.fixture()
def widget_card_number():
    return 'Visa Gold 1212121212121212'


@pytest.fixture()
def widget_get_date_base():
    return "2024-03-11T02:26:18.671407"
