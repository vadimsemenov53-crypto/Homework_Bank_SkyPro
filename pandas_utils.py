import pandas as pd


def read_transactions_from_csv(path_to_file: str) -> list[dict]:
    """Функция принимает путь до файла (path_to_file),
    считывает финансовые операции из CSV-файла и возвращает список словарей.
    Пример для передачи пути: '/Users/PycharmProjects/data/transactions.csv'."""
    try:
        df = pd.read_csv(path_to_file)

        list_data = df.to_dict(orient="records")
        return list_data

    except ValueError:
        print("Передан не верный формат")
        return []

    except FileNotFoundError:
        print("Файл не найден")
        return []


def read_transactions_from_excel(path_to_file: str) -> list[dict]:
    """Функция принимает путь до файла (path_to_file),
    считывает финансовые операции из Excel-файла и возвращает список словарей.
    Пример для передачи пути: '/Users/PycharmProjects/data/transactions_excel.xlsx'."""
    try:
        df = pd.read_excel(path_to_file)

        list_data = df.to_dict(orient="records")
        return list_data

    except ValueError:
        print("Передан не верный формат")
        return []

    except FileNotFoundError:
        print("Файл не найден")
        return []
