import pytest

from src.generators import filter_by_currency, transaction_descriptions

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
                {"operationAmount": {"currency": {"code": "EUR"}},
                 "description": "Перевод организации"},
                {"operationAmount": {"currency": {"code": "USD"}},
                 "description": "Перевод с карты на карту"},
                {"operationAmount": {"currency": {"code": "EUR"}},
                 "description": "Анонимный перевод"}
            ],
            'EUR',
            'Перевод организации, Перевод с карты на карту, Анонимный перевод'
    )
])
def test_filter_by_currency_another_data(transactions_info, currency, expected):
    gen = filter_by_currency(transactions_info, currency)
    assert next(gen) == {'operationAmount': {'currency': {'code': 'EUR'}}, 'description': 'Перевод организации'}
    assert next(gen) == {'operationAmount': {'currency': {'code': 'EUR'}}, 'description': 'Анонимный перевод'}
    with pytest.raises(StopIteration):
        assert next(gen)


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


def test_transaction_descriptions_base(generators_data):
    gen = transaction_descriptions(generators_data)
    assert next(gen) == 'Перевод организации'
    assert next(gen) == 'Перевод со счета на счет'
    assert next(gen) == 'Перевод со счета на счет'
    assert next(gen) == 'Перевод с карты на карту'
    assert next(gen) == 'Перевод организации'
    with pytest.raises(StopIteration):
        next(gen)


@pytest.mark.parametrize('transactions_info, expected',
[
    (
        [
            {"operationAmount": {"currency": {"code": "RUB"}},
        "description": "Перевод организации"},
        {"operationAmount": {"currency": {"code": "USD"}},
        "description": "Перевод с карты на карту"},
        {"operationAmount": {"currency": {"code": "EUR"}},
        "description": "Анонимный перевод"}
        ],
        'Перевод организации, Перевод с карты на карту, Анонимный перевод'
    )
])
def test_transaction_descriptions_another_info(transactions_info, expected):
    gen = transaction_descriptions(transactions_info)
    assert next(gen) == 'Перевод организации'
    assert next(gen) == 'Перевод с карты на карту'
    assert next(gen) == 'Анонимный перевод'
    with pytest.raises(StopIteration):
        next(gen)


def test_transaction_descriptions_empty_list():
    gen = transaction_descriptions([])
    assert next(gen) == 'Нет данных'
    with pytest.raises(StopIteration):
        next(gen)



