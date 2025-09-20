from src.widget import get_date, mask_account_card

get_account_card = input("Введите вид счёта или карты и его/её номер - ")
get_date_time = input("Введите строку даты и времени - ")

print(mask_account_card(get_account_card))
print(get_date(get_date_time))
