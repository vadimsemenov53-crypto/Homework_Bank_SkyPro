import os
from functools import wraps
from time import time
from typing import Any, Callable


def log(filename: str = "") -> Callable[..., Any]:
    def wrapper(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            start_time = time()

            try:
                result = func(*args, **kwargs)
                end_time = time()
                func_data = f"""Функция: {func.__name__}.
Вызвана с аргументами {args}, и ключевыми аргументами {kwargs}.
Результат: {result}
Время работы = {end_time - start_time:.6f}"""
                flag = True

            except Exception as error:
                end_time = time()
                func_data = f"""Функция: {func.__name__}.
Вызвана с аргументами {args}, и ключевыми аргументами {kwargs}.
Тип ошибки: {type(error).__name__}
Время до ошибки = {end_time - start_time:.6f}"""
                flag = False

            if filename:
                if not isinstance(filename, str):
                    raise TypeError("Имя файла должно быть строкой")

                print(f"Данные записаны в файл -> {filename}")

                path_data = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
                path_full = os.path.join(path_data, filename)
                with open(path_full, "a", encoding="utf-8") as file:
                    file.write(f"{func_data}\n")
                    file.write(f"{'-' * 80}\n")

            else:
                print(func_data)

            if flag:
                return func(*args, **kwargs)
            else:
                raise

        return inner

    return wrapper
