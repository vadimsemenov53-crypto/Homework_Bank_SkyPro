from unittest.mock import Mock, patch

import pytest
from requests import RequestException

from external_api import get_amount_in_rubles


def test_get_amount_in_rubles_base_rub(transaction_data_rub):
    assert get_amount_in_rubles(transaction_data_rub) == 1000.0


def test_get_amount_in_rubles_base_usd(transaction_data_usd):
    mock_get = Mock()
    mock_get.status_code = 200
    mock_get.json.return_value = {"result": 2100.45}

    with patch("requests.get", return_value=mock_get):
        result = get_amount_in_rubles(transaction_data_usd)
        assert result == 2100.45


@patch("external_api.requests.get")
def test_get_amount_in_rubles_invalid_status(mock_get, transaction_data_usd):
    mock_get.return_value.status_code = 400
    mock_get.json.return_value = {"result": 2100.45}

    with pytest.raises(RequestException, match="Ошибка API: 400"):
        assert get_amount_in_rubles(transaction_data_usd)


def test_get_amount_in_rubles_invalid_key():
    transaction_invalid = {"operation": {"amount": "1000", "currency": {"name": "usd", "code": "USD"}}}
    with pytest.raises(KeyError, match="Ключ не найден: 'operationAmount'"):
        get_amount_in_rubles(transaction_invalid)
