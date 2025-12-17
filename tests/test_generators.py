import pytest

from src.generators import filter_by_currency

def test_filter_by_currency_base(generators_data):
    gen = filter_by_currency(generators_data, 'USD')

    assert next(gen) == {'date': '2018-06-30T02:08:58.425572',
 'description': 'Перевод организации',
 'from': 'Счет 75106830613657916952',
 'id': 939719570,
 'operationAmount': {'amount': '9824.07',
                     'currency': {'code': 'USD', 'name': 'USD'}},
 'state': 'EXECUTED',
 'to': 'Счет 11776614605963066702'}

    assert next(gen) == {'date': '2019-04-04T23:20:05.206878',
 'description': 'Перевод со счета на счет',
 'from': 'Счет 19708645243227258542',
 'id': 142264268,
 'operationAmount': {'amount': '79114.93',
                     'currency': {'code': 'USD', 'name': 'USD'}},
 'state': 'EXECUTED',
 'to': 'Счет 75651667383060284188'}

    assert next(gen) == {'date': '2018-08-19T04:27:37.904916',
 'description': 'Перевод с карты на карту',
 'from': 'Visa Classic 6831982476737658',
 'id': 895315941,
 'operationAmount': {'amount': '56883.54',
                     'currency': {'code': 'USD', 'name': 'USD'}},
 'state': 'EXECUTED',
 'to': 'Visa Platinum 8990922113665229'}

    with pytest.raises(StopIteration):
        assert next(gen)

@pytest.mark.parametrize('transactions_info, currency, expected',
[
    (
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "руб",
                        "code": "RUB"
                    }
                }
            }
        ]
    ,
    'RUB',
    [{
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "руб",
                "code": "RUB"
                         }
                }
        }]
    )
])
def test_filter_by_currency_another_data(transactions_info, currency, expected):
    assert list(filter_by_currency(transactions_info, currency)) == expected


def test_filter_by_currency_case_sensitive():
    result = list(filter_by_currency([
        {"operationAmount": {"currency": {"code": "RUB"}}
        }],
        'rub'))
    assert result == [{'operationAmount': {'currency': {'code': 'RUB'}}}]


def test_filter_by_currency_no_matches():
    result = list(filter_by_currency([
        {"operationAmount": {"currency": {"code": "RUB"}}
        },
        {"operationAmount": {"currency": {"code": "USD"}}
         }
    ],
        'EUR'))
    assert result == []


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], 'USD'))
    assert result == []

