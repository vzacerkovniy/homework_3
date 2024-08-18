import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_transaction_descriptions(transactions_list: list):
    gen = transaction_descriptions(transactions_list)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод с карты на карту"
    assert next(gen) == "Перевод организации"


def test_transaction_empty(list_empty: list):
    gen = transaction_descriptions(list_empty)
    assert next(gen) == "Неверный ввод"


@pytest.mark.parametrize(
    "start, end",
    [
        (0, 5),
    ],
)
def test_card_number_generator(start: int, end: int):
    a = card_number_generator(start, end)
    assert next(a) == "0000 0000 0000 0000"
    assert next(a) == "0000 0000 0000 0001"
    assert next(a) == "0000 0000 0000 0002"
    assert next(a) == "0000 0000 0000 0003"
    assert next(a) == "0000 0000 0000 0004"


def test_filter_by_currency_1(transactions_list: list):
    gen_1 = filter_by_currency(transactions_list, "RUB")
    assert next(gen_1) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(gen_1) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


def test_filter_by_currency_2(transactions_list: list):
    gen_2 = filter_by_currency(transactions_list, "USD")
    assert next(gen_2) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(gen_2) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(gen_2) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


def test_filter_by_currency_3(transactions_list: list):
    gen_3 = filter_by_currency(transactions_list, "EUR")
    assert next(gen_3) == ["Валюта не поддерживается"]
