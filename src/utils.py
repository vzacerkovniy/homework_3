import json


def get_json_operations(path: str) -> list[dict]:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными"""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return []
    except ValueError:
        return []
