# Импортируем словарь

import requests as requests

URL = "https://www.jsonkeeper.com/b/0MZI"

result = requests.get(URL).json()


def if_EXECUTED():
    """
    Сортируем все транзакции по Выполненым
    :return: Возврощает отсортированый список
    """
    exc = []
    for i in range(len(result)):
        if "state" not in result[i]:
            continue
        if "from" not in result[i]:
            continue
        if result[i]["state"] == "EXECUTED":
            exc.append(result[i])
    return exc


def last_five():
    """
    Из сортировоного списа берем пять последних по дате
    :return: Возврощает список из 5 транзакций
    """
    new = if_EXECUTED()[::-1]
    lis_new = sorted(new[:5], key=lambda data: data["date"])
    return lis_new[::-1]


def data_time(data):
    """
    Делаем дату из словаря
    :param data: строчка из словаря с датой
    :return:дата (день, месяц, год)
    """
    data = data.split("-")
    index_data_2 = [data[2][:2], data[1], data[0]]
    return ".".join(index_data_2)


def organization_transfer(description):
    """
    Организация транзакции
    :param description: строка из словаря
    :return: транзакция
    """
    return description


def number_cart_send(send):
    """
    Выводим Номер карты и систему оплаты
    :param send: номер счёта отправителя
    :return: возврощает скрытый счёт
    """
    account_number = send.split(' ')[-1]
    if len(account_number) == 20:
        return f'Счет **{account_number[16:]}'
    else:
        return f'{" ".join(send.split(" ")[:-1])} ' \
               f'{account_number[0:4]} {account_number[4:6]}' \
               f'** **** {account_number[12:]}'


def number_cart_recipient(recipient):
    """
    Выводим Номер карты и систему оплаты
    :param recipient: номер счёта получателя
    :return: возврощает скрытый счёт
    """
    account_number = recipient.split(' ')[-1]
    if len(account_number) == 20:
        return f'Счет **{account_number[16:]}'
    else:
        return f'{" ".join(recipient.split(" ")[:-1])} ' \
               f'{account_number[0:4]} {account_number[4:6]}' \
               f'** **** {account_number[12:]}'


def money(amount_of_money, currency):
    """
    :param amount_of_money: Вводится колличество денег из словаря
    :param currency: Вводится валюта из словаря
    :return: Возврощает количество денег и волюту
    """
    return f'{amount_of_money} {currency}'

