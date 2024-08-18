def filter_by_currency(transactions: list, currency: str):
    """Функция, фильтрующая список словарей в зависимости от кода валюты"""
    list_usd = []
    list_rub = []
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == "USD":
            list_usd.append(transaction)
        elif transaction["operationAmount"]["currency"]["code"] == "RUB":
            list_rub.append(transaction)
    if currency == "USD":
        for usd in list_usd:
            yield usd
    elif currency == "RUB":
        for rub in list_rub:
            yield rub
    else:
        yield ["Валюта не поддерживается"]


# print(*filter_by_currency(transactions, "USD"))
# print(*filter_by_currency(transactions, "RUB"))


def transaction_descriptions(transactions: list):
    """Функция-генератор, выводящая описание операции по запросу"""
    if not transactions:
        yield "Неверный ввод"
    else:
        for transaction in transactions:
            yield transaction["description"]


def card_number_generator(start: int, end: int):
    """Функция-генератор номеров банковских карт в формате хххх хххх хххх хххх"""
    for num in range(start, end):
        number = str(format(num, "016"))
        number_gen = number[0:4] + " " + number[4:8] + " " + number[8:12] + " " + number[12:16]
        yield number_gen


# for num in card_number_generator(0, 10000000000000000):
#     print(num)
