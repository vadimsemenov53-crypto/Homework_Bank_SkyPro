from time import time
from functools import wraps


def log(filename = ''):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            start_time = time()

            try:
                result = func(*args, **kwargs)
                end_time = time()
                func_data = f'''Функция: {func.__name__}, вызвана с аргументами {args}, и ключевыми аргументами {kwargs}.
Результат: {result}
Время работы = {end_time - start_time:.6f}'''
                flag = True

            except Exception as error:
                end_time = time()
                func_data = f'''Функция: {func.__name__}, вызвана с аргументами {args}, и ключевыми аргументами {kwargs}.
Тип ошибки: {type(error).__name__}
Время до ошибки = {end_time - start_time:.6f}'''
                flag = False


            if filename:
                if not isinstance(filename, str):
                    raise TypeError('Имя файла должно быть строкой')

                print(f'Данные записаны в файл -> {filename}')

                with open(filename, 'a', encoding="utf-8") as file:
                    file.write(f'{func_data}\n')
                    file.write(f"{'-' * 80}\n")

            else:
                print(func_data)

            if flag:
                return func(*args, **kwargs)
            else:
                raise
        return inner
    return wrapper



@log(filename='data.txt')
def example(*nums):
    """Функция передачи данных"""
    raise ValueError('Сгенерированная ошибка')

example(2, 3, 4, 5)
