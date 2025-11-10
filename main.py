import re

from src.generators import filter_by_currency, filter_by_currency_csv_excel
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import json_file_processing, read_transaction_csv, read_transaction_excel
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON - файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    while True:
        choise_file = input("Выбор 1-3: ")
        if choise_file > "0" and choise_file < "4":
            break

    if choise_file == "1":
        print("Для обработки выбран JSON-файл")
        data_of_transactions = json_file_processing("../data/operations.json")
    elif choise_file == "2":
        print("Для обработки выбран CSV-файл")
        data_of_transactions = read_transaction_csv("../data/transactions.csv", ";")
    else:
        print("Для обработки выбран XLSX-файл")
        data_of_transactions = read_transaction_excel("../data/transactions_excel.xlsx")

    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтровки статусы:")
    print("1. EXECUTED")
    print("2. CANCELED")
    print("3. PENDING")
    while True:
        choise_status = input("Выбор 1-3: ")
        if choise_status > "0" and choise_status < "4":
            break
        print("Выбран не верный статус. Выберите из предложенного: EXECUTE, CANCELED, PENDING")
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы:")
        print("1. EXECUTED")
        print("2. CANCELED")
        print("3. PENDING")

    if choise_status == "1":
        data_filtered_by_state = filter_by_state(data_of_transactions, "EXECUTED")
        print("Операции отфильтрованы по статусу EXECUTED")
    elif choise_status == "2":
        data_filtered_by_state = filter_by_state(data_of_transactions, "CANCELED")
        print("Операции отфильтрованы по статусу CANCELED")
    else:
        data_filtered_by_state = filter_by_state(data_of_transactions, "PENDING")
        print("Операции отфильтрованы по статусу PENDING")

    if len(data_filtered_by_state) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        quit()

    while True:
        choise_sort_day = input("Отсортировать операции по дате? Да/Нет (Д/н) ").lower()
        if choise_sort_day == "да" or choise_sort_day == "д" or choise_sort_day == "нет" or choise_sort_day == "н":
            break

    if choise_sort_day == "да" or choise_sort_day == "д":
        while True:
            choise_sort_day_ = input("Отсортировать по убыванию? Да/Нет (Д/н) ").lower()
            if (
                choise_sort_day_ == "да"
                or choise_sort_day_ == "д"
                or choise_sort_day_ == "нет"
                or choise_sort_day_ == "н"
            ):
                break

        if choise_sort_day_ == "да" or choise_sort_day_ == "д":
            data_sorted_by_date = sort_by_date(data_filtered_by_state, True)
        else:
            data_sorted_by_date = sort_by_date(data_filtered_by_state, False)

    if choise_sort_day == "да" or choise_sort_day == "д":
        data_before_choosing_operations = data_sorted_by_date
    else:
        data_before_choosing_operations = data_filtered_by_state

    while True:
        choise_operation_rub = input("Выводить только рублевые транзакции? Да/Нет (Д/н) ").lower()
        if (
            choise_operation_rub == "да"
            or choise_operation_rub == "д"
            or choise_operation_rub == "нет"
            or choise_operation_rub == "н"
        ):
            break

    if choise_operation_rub == "да" or choise_operation_rub == "д":
        if choise_file == "1":
            generator_operations = list(filter_by_currency(data_before_choosing_operations, "RUB"))
        else:
            generator_operations = list(filter_by_currency_csv_excel(data_before_choosing_operations, "RUB"))
    else:
        generator_operations = data_before_choosing_operations

    if len(generator_operations) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        quit()

    while True:
        choise_sort_word = input(
            "Отфильтровать список транзакций по определенному слову \
в описании? Да/Нет (Д/н) "
        ).lower()
        if choise_sort_word == "да" or choise_sort_word == "д" or choise_sort_word == "нет" or choise_sort_word == "н":
            break

    if choise_sort_word == "да" or choise_sort_word == "д":
        choise_sort_word_ = input("По какому слову отфильтровать транзакции? ")
        result = process_bank_search(generator_operations, choise_sort_word_)
    else:
        result = generator_operations

    if len(result) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        quit()

    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(result)}\n")

    for item in result:
        print(f"{get_date(item['date'])} {item['description']}")
        if re.search("Открытие", item["description"], flags=re.IGNORECASE) is None:
            print(f"{mask_account_card(item['from'])} -> {mask_account_card(item['to'])}")
        else:
            print(f"{mask_account_card(item['to'])}")
        if choise_file == "1":
            print(f"Сумма: {item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n")
        else:
            print(f"Сумма: {item['amount']} {item['currency_name']}\n")
