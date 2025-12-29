from time import time
from functools import wraps


def log(filename = ''):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            start_time = time()
            result = func(*args, **kwargs)
            end_time = time()

            func_data = f'''Функция: {func.__name__}, вызвана с аргументами {args}, и клюевыми аргументами {kwargs}.
Результат: {result}'''
            time_work = f'Время работы = {end_time - start_time:.6f}'

            if filename:
                if type(filename) == str:
                    file_record = filename + '.txt'
                    print(f'Переданный файл для записи -> {file_record}')

                    with open(file_record, 'a', encoding="utf-8") as file:
                        file.write(f'{func_data}\n')
                        file.write(f'{time_work}\n')
                        file.write(f"{'-' * 80}\n")
                        return result

                else:
                    raise TypeError('Передан неверный тип данный (отличный от "str")')

            print(func_data)
            print(time_work)
            return result
        return inner
    return wrapper


@log(filename='data')
def example(*nums):
    return [x for x in nums if x % 2 == 0]

example(2, 4, 5, 6, 7)

