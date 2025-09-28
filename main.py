from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

list_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

get_account_card = input("Введите вид счёта или карты и его/её номер - ")
get_date_time = input("Введите строку даты и времени - ")

print(mask_account_card(get_account_card))
print(get_date(get_date_time))
print(filter_by_state(list_data))
print(sort_by_date(list_data))
