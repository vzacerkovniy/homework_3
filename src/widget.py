from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция, возвращающая маску карты или счета"""
    if "Счет" in number:
        return get_mask_account(number)
    else:
        return get_mask_card_number(number)


def get_data(data: str) -> str:
    """Функция, возвращающая дату в фотраме дд.мм.гггг"""
    no_symbol_str = data.replace(":", "").replace("-", "").replace(".", "").replace("T", "")
    if data != "" and no_symbol_str.isdigit():
        new_data = no_symbol_str[6:8] + "." + no_symbol_str[4:6] + "." + no_symbol_str[0:4]
        return new_data
    return "Неверный ввод"
