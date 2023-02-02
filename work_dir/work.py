from fun import *


def work_proj():
    for item in last_five():
        print(data_time(item["date"]), organization_transfer(item['description']))
        print(f'{number_cart_send(item["from"])} -> {number_cart_recipient(item["to"])}')
        print(item["operationAmount"]["amount"], item["operationAmount"]["currency"]["name"])
        print()

work_proj()













