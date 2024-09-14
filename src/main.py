from csv_pandas import get_from_csv, get_from_excel
from utils import get_json_operations
from processing import filter_by_state, sort_by_date, filter_by_currency
from search import search_by_pattern
from widget import mask_account_card


def main():
    """Главная функция программы"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    user_request = input("""Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n""")

    # Для JSON варианта
    if user_request == "1":
        print("Для обработки выбран JSON-файл.")
        way = input("Укажите путь к JSON файлу: \n")
        json_program = get_json_operations(way)
        status = ""
        while status != "EXECUTED" or "CANCELED" or "PENDING":
            status = input("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n""").upper()
            if status == "EXECUTED":
                print('Операции отфильтрованы по статусу "EXECUTED"')
                filter_by_state(json_program, status)
                break
            elif status == "CANCELED":
                print('Операции отфильтрованы по статусу "CANCELED"')
                filter_by_state(json_program, status)
                break
            elif status == "PENDING":
                print('Операции отфильтрованы по статусу "PENDING"')
                filter_by_state(json_program, status)
                break
            else:
                print(f"Статус операции \"{status}\" недоступен.\n")

        is_sort = input("Отсортировать операции по дате? Да/Нет\n").lower()
        date = []
        if is_sort == "да":
            order = input("Отсортировать по возрастанию или по убыванию?\n").lower()
            if order == "по возрастанию":
                date = sort_by_date(filter_by_state(json_program, status), True)
            else:
                date = sort_by_date(filter_by_state(json_program, status), False)

        is_rub = input("Выводить только рублевые тразакции? Да/Нет\n").lower()
        if is_rub == "rub":
            filter_by_currency(date, "RUB")

        is_keyword = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
        result = []
        if is_keyword == "да":
            keyword = input("Введите слово:\n")
            result = search_by_pattern(filter_by_currency(date, "RUB"), keyword)
        if len(result) != 0:
            print("Распечатываю итоговый список транзакций...\n")
            print(f"Всего банковских операций в выборке: {len(result)}\n")
            for i in result:
                print(f"{i["date"]} {i["description"]}")
                print(f"{mask_account_card(str(i["from"]))} -> {mask_account_card(str(i["to"]))}")
                print(f"Сумма: {i["amount"]} {i["currency_code"]}\n")
        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    # Для CSV варианта
    elif user_request == "2":
        print("Для обработки выбран CSV-файл.")
        way = input("Укажите путь к CSV файлу: \n")
        csv_program = get_from_csv(way)
        status = ""
        while status != "EXECUTED" or "CANCELED" or "PENDING":
            status = input("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n""").upper()
            if status == "EXECUTED":
                print('Операции отфильтрованы по статусу "EXECUTED"')
                filter_by_state(csv_program, status)
                break
            elif status == "CANCELED":
                print('Операции отфильтрованы по статусу "CANCELED"')
                filter_by_state(csv_program, status)
                break
            elif status == "PENDING":
                print('Операции отфильтрованы по статусу "PENDING"')
                filter_by_state(csv_program, status)
                break
            else:
                print(f"Статус операции \"{status}\" недоступен.\n")

        is_sort = input("Отсортировать операции по дате? Да/Нет\n").lower()
        date = []
        if is_sort == "да":
            order = input("Отсортировать по возрастанию или по убыванию?\n").lower()
            if order == "по возрастанию":
                date = sort_by_date(filter_by_state(csv_program, status), True)
            else:
                date = sort_by_date(filter_by_state(csv_program, status), False)

        is_rub = input("Выводить только рублевые тразакции? Да/Нет\n").lower()
        if is_rub == "rub":
            filter_by_currency(date, "RUB")

        is_keyword = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
        result = []
        if is_keyword == "да":
            keyword = input("Введите слово:\n")
            result = search_by_pattern(filter_by_currency(date, "RUB"), keyword)
        if len(result) != 0:
            print("Распечатываю итоговый список транзакций...\n")
            print(f"Всего банковских операций в выборке: {len(result)}\n")
            for i in result:
                print(f"{i["date"]} {i["description"]}")
                print(f"{mask_account_card(str(i["from"]))} -> {mask_account_card(str(i["to"]))}")
                print(f"Сумма: {i["amount"]} {i["currency_code"]}\n")
        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    # Для XLSX варианта
    elif user_request == "3":
        print("Для обработки выбран XLSX-файл.")
        way = input("Укажите путь к XLSX файлу: \n")
        xlsx_program = get_from_excel(way)
        status = ""
        while status != "EXECUTED" or "CANCELED" or "PENDING":
            status = input("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n""").upper()
            if status == "EXECUTED":
                print('Операции отфильтрованы по статусу "EXECUTED"')
                filter_by_state(xlsx_program, status)
                break
            elif status == "CANCELED":
                print('Операции отфильтрованы по статусу "CANCELED"')
                filter_by_state(xlsx_program, status)
                break
            elif status == "PENDING":
                print('Операции отфильтрованы по статусу "PENDING"')
                filter_by_state(xlsx_program, status)
                break
            else:
                print(f"Статус операции \"{status}\" недоступен.\n")

        is_sort = input("Отсортировать операции по дате? Да/Нет\n").lower()
        date = []
        if is_sort == "да":
            order = input("Отсортировать по возрастанию или по убыванию?\n").lower()
            if order == "по возрастанию":
                date = sort_by_date(filter_by_state(xlsx_program, status), True)
            else:
                date = sort_by_date(filter_by_state(xlsx_program, status), False)

        is_rub = input("Выводить только рублевые тразакции? Да/Нет\n").lower()
        if is_rub == "rub":
            filter_by_currency(date, "RUB")

        is_keyword = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
        result = []
        if is_keyword == "да":
            keyword = input("Введите слово:\n")
            result = search_by_pattern(filter_by_currency(date, "RUB"), keyword)
        if len(result) != 0:
            print("Распечатываю итоговый список транзакций...\n")
            print(f"Всего банковских операций в выборке: {len(result)}\n")
            for i in result:
                print(f"{i["date"]} {i["description"]}")
                print(f"{mask_account_card(str(i["from"]))} -> {mask_account_card(str(i["to"]))}")
                print(f"Сумма: {i["amount"]} {i["currency_code"]}\n")
        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


main()