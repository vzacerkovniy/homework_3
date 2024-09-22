def get_mask_card_number(number: str) -> str:
    """Функция, возвращающая маску карты"""
    no_space_num = number.replace(" ", "")
    num_str = ""
    for sym in number:
        if sym.isdigit():
            num_str += sym
    if (
        no_space_num != ""
        and no_space_num.isdigit() is False
        and no_space_num.isalpha() is False
        and len(num_str) == 16
    ):
        card_mask = (
            no_space_num[:-16]
            + " "
            + no_space_num[-16:-12]
            + " "
            + no_space_num[-12:-10]
            + "** **** "
            + no_space_num[-4:]
        )
        return card_mask
    else:
        pass


def get_mask_account(number: str) -> str:
    """Функция, возвращающая маску счета"""
    no_space_num = number.replace(" ", "")
    num_str = ""
    for sym in number:
        if sym.isdigit():
            num_str += str(sym)
    if (
        no_space_num != ""
        and no_space_num.isdigit() is False
        and no_space_num.isalpha() is False
        and len(num_str) == 20):
        account_mask = "Счет **" + num_str[-4:]
        return account_mask
    else:
        pass
