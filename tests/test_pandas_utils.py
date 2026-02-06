import pandas as pd
import os
from unittest.mock import patch
from pandas_utils import read_transactions_from_csv, read_transactions_from_excel

@patch('pandas_utils.pd.read_csv')
def test_read_transactions_from_csv_base(mock_get, data_for_csv_xlsx):
    mock_get.return_value = pd.DataFrame(data_for_csv_xlsx)

    result = read_transactions_from_csv('/Users/file')
    assert result == data_for_csv_xlsx


@patch('pandas_utils.pd.read_csv')
def test_read_transactions_from_csv_empty(mock_get):
    mock_get.return_value = pd.DataFrame([{}])

    result = read_transactions_from_csv('user/file')
    assert result == []


def test_read_transactions_from_csv_file_not_found():
    assert read_transactions_from_csv('user/fake_path') == []


def test_read_transactions_from_csv_file_wrong():
    path_base = os.path.dirname(__file__)
    path_to_file = os.path.join(path_base, 'data/transactions_excel.xlsx')

    assert read_transactions_from_csv(path_to_file) == []


@patch('pandas_utils.pd.read_csv')
def test_read_transactions_from_csv_value_error(mock_get):
    mock_get.side_effect = ValueError
    result = read_transactions_from_csv('user/file')
    assert result == []


@patch('pandas_utils.pd.read_excel')
def test_read_transactions_from_excel_base(mock_get, data_for_csv_xlsx):
    mock_get.return_value = pd.DataFrame(data_for_csv_xlsx)

    result = read_transactions_from_excel('user/file')
    assert result == data_for_csv_xlsx


@patch('pandas_utils.pd.read_excel')
def test_read_transactions_from_excel_empty(mock_get):
    mock_get.return_value = pd.DataFrame([{}])

    result = read_transactions_from_excel('user/file')
    assert result == []


def test_read_transactions_from_excel_file_not_found():
    assert read_transactions_from_excel('user/fake_path') == []


def test_read_transactions_from_exel_file_wrong():
    path_base = os.path.dirname(__file__)
    path_to_file = os.path.join(path_base, 'data/transactions.csv')

    assert read_transactions_from_excel(path_to_file) == []


@patch('pandas_utils.pd.read_excel')
def test_read_transactions_from_excel_value_error(mock_get):
    mock_get.side_effect = ValueError
    result = read_transactions_from_excel('user/file')
    assert result == []