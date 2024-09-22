def filter_by_state(input_list: list, status: str = "CANCELED") -> list:
    """Функция фильтрации списка словарей по значению ключа"""
    current_state = []
    for operation in input_list:
        if operation["state"] == status:
            current_state.append(operation)
        else:
            pass
    return current_state


def sort_by_date(input_list: list, ascending: bool = True) -> list:
    """Функция сортировки списка словарей по убыванию даты"""
    if ascending is False:
        output_list = sorted(input_list, key=lambda dic: dic["date"], reverse=False)
        return output_list
    else:
        output_list = sorted(input_list, key=lambda dic: dic["date"], reverse=True)
        return output_list


def filter_by_currency(input_list: list, currency: str) -> list:
    """Функция фильтрации списка словарей по валюте"""
    current_currency = []
    for operation in input_list:
        if operation["currency_code"] == currency:
            current_currency.append(operation)
        else:
            pass
    return current_currency
