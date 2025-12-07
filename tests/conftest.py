import pytest


@pytest.fixture()
def card_number():
    return "2202001366664707"


@pytest.fixture()
def number_account():
    return "271728141201"


@pytest.fixture()
def widget_account_number():
    return "Счет 474733892717"


@pytest.fixture()
def widget_card_number():
    return "Visa Gold 1212121212121212"


@pytest.fixture()
def widget_get_date_base():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture()
def processing():
    info_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    return info_list
