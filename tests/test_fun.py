from fun import (result,
                 if_EXECUTED,
                 last_five,
                 data_time,
                 organization_transfer,
                 number_cart_send,
                 number_cart_recipient,
                 money)


def test_transaction_if_EXECUTED():
    assert if_EXECUTED() != result


def test_last_five():
    assert len(last_five()) == 5
    assert len(last_five()) != 6
    assert len(last_five()) != 4
    assert last_five() != if_EXECUTED()


def test_data_time():
    assert data_time("2019-07-13T18:51:29.313309") == "13.07.2019"
    assert data_time("2019-05-19T12:51:49.023880") == "19.05.2019"
    assert data_time("2019-01-05T00:52:30.108534") == "05.01.2019"
    assert data_time("2018-12-22T02:02:49.564873") == "22.12.2018"
    assert data_time("2018-03-09T23:57:37.537412") == "09.03.2018"


def test_organization_transfer():
    assert organization_transfer("Перевод организации") == "Перевод организации"
    assert organization_transfer("Открытие вклада") == "Открытие вклада"
    assert organization_transfer("Перевод со счета на счет") == "Перевод со счета на счет"
    assert organization_transfer("Перевод со счета на счет") != "Открытие вклада"


def test_number_cart_send():
    assert number_cart_send("Счет 26406253703545413262") == "Счет **3262"
    assert len(number_cart_send("Счет 26406253703545413262")) == 11
    assert number_cart_send("Visa Gold 8326537236216459") == "Visa Gold 8326 53** **** 6459"


def test_number_cart_recipient():
    assert number_cart_recipient("Счет 26406253703545413262") == "Счет **3262"
    assert len(number_cart_recipient("Счет 26406253703545413262")) == 11
    assert number_cart_recipient("Visa Gold 8326537236216459") == "Visa Gold 8326 53** **** 6459"


def test_money():
    assert money("25780.71", "руб.") == "25780.71 руб."

