import datetime
import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import sum_to_convert

load_dotenv(".env")
api_key = os.getenv("API_KEY")
time_now = datetime.datetime.now().strftime("%Y-%m-%d")


@patch("requests.get")
def test_sum_to_convert(mock_get):
    """ test """
    mock_get.return_value.json.return_value = {"result": 31957.58}
    assert (
        sum_to_convert(
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                }
            ],
            time_now,
            api_key,
        )
        == float(31957.58)
    )
    mock_get.assert_called_once_with(
        f"https://api.apilayer.com/fixer/convert?base=RUB \
                                                                          &symbols=RUB \
                                                                          &amount=31957.58 \
                                                                          &date={time_now} \
                                                                          &apikey: {api_key}"
    )
