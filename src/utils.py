import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log")
file_formater = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_json_operations(path: str) -> list[dict]:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными"""
    try:
        logger.debug(f"Выводим данные из файла {path}")
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        logger.error("Файл не найден")
        return []
    except ValueError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []
