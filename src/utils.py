import json
# import os

# data_path = os.path.join(os.path.dirname(__file__), "..", 'data', 'operations.json')


def get_json_operations(data_path: str) -> list[dict]:
    """ Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными """
    try:
        with open(data_path, encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print([])
    except ValueError:
        print([])


# print(get_json_operations(data_path))
