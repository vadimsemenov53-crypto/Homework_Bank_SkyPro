from src.utils import get_operations
from pandas_utils import read_transactions_from_csv, read_transactions_from_excel
from src.processing import filter_by_state, sort_by_date
from src.operations import filter_operations_by_description
from src.widget import mask_account_card

VALID_STATUSES = ["EXECUTED", "CANCELED", "PENDING"]

def main() -> None:
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
        print("Программа: По заданному пути файл не найден.")
        return

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
    choice_currency = str(input('Пользователь : ')).upper().strip()

    if choice_currency == 'ДА':
        result_filter = [
            trans for trans in result_filter
            if trans["operationAmount"]["currency"]["code"] == 'RUB'
        ]

    print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    choice_description = str(input('Пользователь : ')).upper().strip()

    if choice_description == 'ДА':
        print("Программа: По какому слову в описании будем фильтровать?")
        word_user = str(input('Пользователь : ')).strip()

        result_filter = filter_operations_by_description(result_filter, word_user)

    print(f"""Программа: Распечатываю итоговый список транзакций...
Программа: Всего банковских операций в выборке: {len(result_filter)}""")

    for transaction in result_filter:
        if transaction['description'] == 'Открытие вклада':
            print(f"{transaction['date'][:10]} {transaction['description']}")
            print(f"{mask_account_card(transaction['to'])}")
            print(f"Сумма: {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}")
        else:
            print(f"{transaction['date'][:10]} {transaction['description']}")
            print(f"{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}")
            print(f"Сумма: {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}")





if __name__ == '__main__':
    main()