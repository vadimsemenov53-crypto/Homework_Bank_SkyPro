from src.utils import get_operations
from pandas_utils import read_transactions_from_csv, read_transactions_from_excel
from src.processing import filter_by_state, sort_by_date

VALID_STATUSES = ["EXECUTED", "CANCELED", "PENDING"]

def main():
    print("""Программа: Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
""")
    choice = int(input('Пользователь : '))
    if choice == 1:
        print("""Программа: Для обработки выбран JSON-файл.
            Передайте путь до файла.""")

        path_file = str(input("Пользователь : "))
        data_operations = get_operations(path_file)

    elif choice == 2:
        print("""Программа: Для обработки выбран CSV-файл.
                    Передайте путь до файла.""")

        path_file = str(input("Пользователь : "))
        data_operations = read_transactions_from_csv(path_file)

    elif choice == 3:
        print("""Программа: Для обработки выбран XLSX-файл.
                    Передайте путь до файла.""")

        path_file = str(input("Пользователь : "))
        data_operations = read_transactions_from_excel(path_file)

    if not data_operations:
        return "Программа: По заданному пути файл не найден."

    print("""Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
        """)

    while True:
        status_filter = input("Пользователь : ").upper().strip()
        if status_filter in VALID_STATUSES:
            break

        print(f'Программа: Статус операции {status_filter} недоступен.')

    result_filter = filter_by_state(data_operations, status_filter)

    print("Программа: Отсортировать операции по дате? Да/Нет")
    choice_date = str(input('Пользователь : ').upper().strip())
    if choice_date == 'ДА':
        print("Программа: Отсортировать по возрастанию? Да/Нет")

        choice_reverse = str(input('Пользователь : ')).upper().strip()

        if choice_reverse == 'ДА':
            result_filter = sort_by_date(result_filter, False)
        elif choice_reverse == 'НЕТ':
            result_filter = sort_by_date(result_filter, True)

    print("Программа: Выводить только рублевые транзакции? Да/Нет")

    return result_filter




if __name__ == '__main__':
    print(main())