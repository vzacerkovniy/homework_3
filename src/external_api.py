import requests


def sum_to_convert(oper_list: list[dict], time: str, api_key: str) -> float:
    """Функция по выводу сумм транзакций в рублях"""
    for operation in oper_list:
        base_amount = operation["operationAmount"]["amount"]
        code = operation["operationAmount"]["currency"]["code"]
        response = requests.get(
            f"https://api.apilayer.com/fixer/convert?base=RUB \
                                                                          &symbols={code} \
                                                                          &amount={base_amount} \
                                                                          &date={time} \
                                                                          &apikey: {api_key}"
        )

        return float(response.json()["result"])
