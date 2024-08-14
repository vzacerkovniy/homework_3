import logging

import requests

logger = logging.getLogger("external_api")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/external_api.log")
file_formater = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def sum_to_convert(oper_dict: dict, api_key: str) -> float:
    """Функция по выводу сумм транзакций в рублях"""
    amount = oper_dict["operationAmount"]["amount"]
    try:
        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/live?base=RUB&symbols=EUR,USD&amount={amount} \
                                                                              &apikey: {api_key}"
        )

        return float(response.json()["result"])
    except ValueError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return 0
