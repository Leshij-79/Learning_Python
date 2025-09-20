from src.masks import get_mask_account, get_mask_card_number

get_account = str(input("Введите номер счёта - "))
get_card_number = str(input("Ввкдите номер карты - "))

print(get_mask_card_number(get_card_number))
print(get_mask_account(get_account))
