from fun import *

def work_proj():
    """
    Рабочий поекст которы принемает тразакции и
    возвращает пять последних выполненных по времени, с датой,
    названием организации, зашифрованым счетом отпровителя и получателя,
    сумму и волюту.
    :return: список выполненых тразакций
    """

    for item in last_five():
        print(data_time(item["date"]), organization_transfer(item['description']))
        print(f'{number_cart_send(item["from"])} -> {number_cart_recipient(item["to"])}')
        print(item["operationAmount"]["amount"], item["operationAmount"]["currency"]["name"])
        print()

work_proj()














