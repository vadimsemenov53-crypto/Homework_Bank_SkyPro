from time import time
from functools import wraps


def log(filename):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            start_time = time()
            result = func(*args, **kwargs)
            end_time = time()

            print(f'Функция: {func.__name__}, вызвана с аргументами {args}, и клюевыми аргументами {kwargs}.'
                  f'Результат: {result}')
            print(f'Время работы = {end_time - start_time:.6f}')
            print(f'Переданный файл для записи -> {filename}')

            return result
        return inner
    return wrapper


@log('result_decorators')
def example(*nums):
    return [x for x in nums if x % 2 == 0]

example(10, 10, 5, 6, 7)

