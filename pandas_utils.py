import pandas as pd

def read_transactions_from_csv(path_to_file: str) -> list[dict]:
    """Функция принимает путь до файла (path_to_file),
    считывает финансовые операции из CSV-файла и возвращает список словарей.
    Пример для передачи пути: '/Users/PycharmProjects/data/transactions.csv'."""
    df = pd.read_csv(path_to_file)

    list_data = df.to_dict(orient='records')
    return list_data


def read_transactions_from_excel(path_to_file: str) -> list[dict]:
    """Функция принимает путь до файла (path_to_file),
    считывает финансовые операции из Excel-файла и возвращает список словарей.
    Пример для передачи пути: '/Users/PycharmProjects/data/transactions_excel.xlsx'."""
    df = pd.read_excel(path_to_file)

    list_data = df.to_dict(orient='records')
    return list_data


if __name__ == '__main__':
    path_csv = '/Users/vadimsemenov/PycharmProjects/Homework_Bank_SkyPro/data/transactions.csv'
    path_xlsx = '/Users/vadimsemenov/PycharmProjects/Homework_Bank_SkyPro/data/transactions_excel.xlsx'

    print(read_transactions_from_excel(path_xlsx))