import json


def get_data():
    """
    Чтение данных из файла json
    """
    with open("../data/operations.json", encoding="utf-8") as file:
        return json.load(file)


def filter_data(data):
    """
    Проверка транзакции на успешность (имеет ли транзакция статус "EXECUTED")
    """
    filter_operations = [operation for operation in data if "state" in operation and operation["state"] == "EXECUTED"]
    return filter_operations


def last_five_operations(data):
    """
    Сортировка и вывод последних 5 операций
    """
    sorted_operations = sorted(data, key=lambda x: x["date"], reverse=True)
    return sorted_operations[:5]


def format_date(date: str):
    """
    Возвращает дату в формате ДД.ММ.ГГГГ
    """
    date_format = date.split("T")[0]
    year, month, day = date_format.split("-")
    return f"{day}.{month}.{year}"


def format_card(card: str):
    """
    Маскировка куска счета звездочками
    """
    card = card.split()
    card_number = card.pop()
    card_name = " ".join(card)
    if card_name.lower() == "счет":
        number_secret = "**" + card_number[-4:]
    else:
        number_secret = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return f"{card_name} {number_secret}"


def get_data_format(data):
    """
    Проверка на наличие информации об отправителе (key: "from") с помощью выше идущей функции, маскирующей часть № карты
    """
    if "from" in data:
        return format_card(data["from"]) + " -> " + format_card(data["to"])
    else:
        return "No card number"


operations_list = get_data()
operations_list = filter_data(operations_list)
last_five_list = last_five_operations(operations_list)
operations = get_data_format(operations_list)

for i in last_five_list:
    """
    Отработка списка последних 5 транзакций для требуемого вывода на печать
    """
    print(f"{format_date(i['date'])} {i['description']}\n"
          f"{get_data_format(i)}\n"
          f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n"
          )
