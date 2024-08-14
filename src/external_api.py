import requests


def sum_to_convert(oper_dict: dict, api_key: str) -> float:
    """Функция по выводу сумм транзакций в рублях"""
    amount = oper_dict["operationAmount"]["amount"]
    response = requests.get(
        f"https://api.apilayer.com/exchangerates_data/live?base=RUB&symbols=EUR,USD&amount={amount} \
                                                                          &apikey: {api_key}"
    )

    return float(response.json()["result"])
