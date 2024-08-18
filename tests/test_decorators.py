import pytest

from src.decorators import log


def predicate_is_int(x):
    return type(x) is int


@log(predicate_is_int, "Значение должно быть целым числом", None)
def square(x):
    """Функция возведения в квадрат"""
    return x * x


with pytest.raises(ValueError, match="Значение должно быть целым числом"):
    square("4")


def test_square_console(capsys):
    square(4)
    captured = capsys.readouterr()
    assert captured.out == "square ok\n"
