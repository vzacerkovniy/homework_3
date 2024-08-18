import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log")
file_formater = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)

def get_mask_card_number(number: str) -> str:
    """Функция, возвращающая маску карты"""
    no_space_num = number.replace(" ", "")
    num_str = ""
    try:
        logger.debug(f"Маскируем номер карты {number}")
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
    except ValueError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return ""


def get_mask_account(number: str) -> str:
    """Функция, возвращающая маску счета"""
    no_space_num = number.replace(" ", "")
    num_str = ""
    try:
        for sym in number:
            logger.debug(f"Маскируем номер счета {number}")
            if sym.isdigit():
                num_str += sym
        if (
            no_space_num != ""
            and no_space_num.isdigit() is False
            and no_space_num.isalpha() is False
            and len(num_str) == 20
        ):
            account_mask = "Счет **" + no_space_num[-4:]
            return account_mask
    except ValueError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return ""
