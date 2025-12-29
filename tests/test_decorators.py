import pytest

from src.decorators import log

def test_return_value():
    @log()
    def add(a, b):
        return a + b


    assert add(4, 1) == 5
    assert add(22.1, 3.2) == 25.3


def test_print_output(capsys):
    @log()
    def square(x):
        return x * x

    square(5)
    captured = capsys.readouterr()
    assert 'Функция: square' in captured.out
    assert 'Вызвана с аргументами (5,), и ключевыми аргументами {}.' in captured.out
    assert 'Результат: 25' in captured.out
    assert 'Время работы =' in captured.out


def test_exception_output(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert 'Функция: divide' in captured.out
    assert 'Вызвана с аргументами (10, 0), и ключевыми аргументами {}.' in captured.out
    assert 'Тип ошибки: ZeroDivisionError' in captured.out
    assert 'Время до ошибки =' in captured.out
