from unittest.mock import patch
from src.csv_pandas import get_from_csv, get_from_excel


@patch('pandas.read_csv')
def test_get_from_csv(mock_read_csv):
    mock_read_csv.return_value.to_dict.return_value = [{'id': '1'}]
    assert get_from_csv('../data/transactions.csv') == [{'id': '1'}]


@patch('pandas.read_excel')
def test_get_from_excel(mock_read_excel):
    mock_read_excel.return_value.to_dict.return_value = [{'id': '1'}]
    assert get_from_excel('../data/transactions_excel.xlsx') == [{'id': '1'}]
