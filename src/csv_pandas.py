import pandas as pd


def get_from_csv(path: str, delimiter: str = ";") -> list:
    """Функция принимает путь до csv-файла и возвращает список словарей с данными"""
    df = pd.read_csv(path, delimiter=delimiter).to_dict(orient="records")
    return df


# print(get_from_csv('../data/transactions.csv'))


def get_from_excel(path: str) -> list:
    """Функция принимает путь до excel-файла и возвращает список словарей с данными"""
    df = pd.read_excel(path).to_dict(orient="records")
    return df


# print(get_from_excel('../data/transactions_excel.xlsx'))
