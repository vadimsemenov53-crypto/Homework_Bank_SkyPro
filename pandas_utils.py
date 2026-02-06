import pandas as pd
import openpyxl

def read_transactions_from_csv(path: str) -> list[dict]:
    """Считывает финансовые операции из CSV-файла и возвращает список словарей."""
    df = pd.read_csv(path)
    return df


def read_transactions_from_excel(path: str) -> list[dict]:
    """Считывает финансовые операции из Excel-файла и возвращает список словарей."""
    df = pd.read_excel(path)
    return df


if __name__ == '__main__':
    path_csv = '/Users/vadimsemenov/PycharmProjects/Homework_Bank_SkyPro/data/transactions.csv'
    path_xlsx = '/Users/vadimsemenov/PycharmProjects/Homework_Bank_SkyPro/data/transactions_excel.xlsx'

    print(read_transactions_from_csv(path_csv))
    print(read_transactions_from_excel(path_xlsx))