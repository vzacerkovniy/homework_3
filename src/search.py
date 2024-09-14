from collections import Counter


def search_by_pattern(transaction_list, key_word):
    """Функция принимает список словарей и возвращает список только тех словарей, в которых найдено ключевое слово"""
    output_list = []
    for transaction in transaction_list:
        if key_word in transaction["description"]:
            output_list.append(transaction)
    return output_list


# print(search_by_pattern([{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
#                           {'id': 3598919.0, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740.0, 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
#                           {'id': 593027.0, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': 30368.0, 'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
#                           {'id': 366176.0, 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': 29482.0, 'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937', 'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'},
#                           {'id': 5380041.0, 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z', 'amount': 23789.0, 'currency_name': 'Peso', 'currency_code': 'UYU', 'from': "nan", 'to': 'Счет 23294994494356835683', 'description': 'Открытие вклада'},
#                           {'id': 1962667.0, 'state': 'EXECUTED', 'date': '2023-10-22T09:43:32Z', 'amount': 18588.0, 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Mastercard 7286844946221431', 'to': 'Счет 76145988629288763144', 'description': 'Перевод организации'},
#                           {'id': 5294458.0, 'state': 'EXECUTED', 'date': '2022-06-20T18:08:20Z', 'amount': 16836.0, 'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Visa 2759011965877198', 'to': 'Счет 38287443300766991082', 'description': 'Перевод с карты на карту'}],
#                         "Перевод организации"))


def search_by_category(transaction_list, category_list):
    """Функция принимает список всех операций и возвращает список с количеством операций в заданных категориях"""
    category_only = []
    for transaction in transaction_list:
        if transaction["description"] in category_list:
            category_only.append(transaction["description"])
    return Counter(i for i in category_list)

# print(search_by_category([{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
#                           {'id': 3598919.0, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740.0, 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
#                           {'id': 593027.0, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': 30368.0, 'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
#                           {'id': 366176.0, 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': 29482.0, 'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937', 'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'},
#                           {'id': 5380041.0, 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z', 'amount': 23789.0, 'currency_name': 'Peso', 'currency_code': 'UYU', 'from': "nan", 'to': 'Счет 23294994494356835683', 'description': 'Открытие вклада'},
#                           {'id': 1962667.0, 'state': 'EXECUTED', 'date': '2023-10-22T09:43:32Z', 'amount': 18588.0, 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Mastercard 7286844946221431', 'to': 'Счет 76145988629288763144', 'description': 'Перевод организации'},
#                           {'id': 5294458.0, 'state': 'EXECUTED', 'date': '2022-06-20T18:08:20Z', 'amount': 16836.0, 'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Visa 2759011965877198', 'to': 'Счет 38287443300766991082', 'description': 'Перевод с карты на карту'}],
#                          ['Перевод организации', 'Открытие вклада']))