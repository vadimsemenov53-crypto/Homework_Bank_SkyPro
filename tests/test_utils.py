import json
from unittest.mock import Mock, patch
from src.utils import get_operations

@patch('src.utils.json.load')
def test_get_operations_base(mock_get, operations_data_fixture):
    mock_get.return_value = operations_data_fixture

    result = get_operations('/Users/vadimsemenov/PycharmProjects/Homework_Bank_SkyPro/data/operations.json')
    assert result == operations_data_fixture


@patch('src.utils.json.load')
def test_get_operations_invalid_data(mock_get):
    data = []
    mock_get.return_value = data
    result = get_operations('/Users/vadimsemenov/PycharmProjects/Homework_Bank_SkyPro/data/operations.json')
    assert result == []


def test_get_operations_file_not_found():
    result = get_operations('/user/data.json')
    assert result == []


@patch('src.utils.json.load')
def test_get_operations_not_list(mock_get):
    mock_get.return_value = {"key": "value"}
    result = get_operations('/Users/vadimsemenov/PycharmProjects/Homework_Bank_SkyPro/data/operations.json')
    assert result == []


@patch('src.utils.json.load')
def test_get_operations_invalid_json(mock_get):
    mock_get.side_effect = json.JSONDecodeError("errorJSONDecode", "", 0)
    result = get_operations('/Users/vadimsemenov/PycharmProjects/Homework_Bank_SkyPro/data/operations.json')
    assert result == []
