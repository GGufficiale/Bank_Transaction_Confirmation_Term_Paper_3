from src.main_and_utils import get_data
from src.main_and_utils import filter_data
from src.main_and_utils import format_date


def test_get_data():
    """
    Проверяет инфрмацию на наличие и на тип (список?)
    """
    data = get_data()
    assert len(data) > 0
    assert type(data) is list


def test_filter_data(operations):
    assert filter_data(operations) == [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }, {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }, ]


def test_format_date():
    assert format_date("2018-06-30T02:08:58.425572") == "30.06.2018"
