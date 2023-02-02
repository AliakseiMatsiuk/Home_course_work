from jeson_file import result
#from datetime import datetime
#from pprint import pprint

def if_EXECUTED():
    exc = []
    for i in range(len(result)):
        if "state" not in result[i]:
            continue
        if "from" not in result[i]:
            continue
        if result[i]["state"] == "EXECUTED":
            exc.append(result[i])
    return exc
#pprint(if_EXECUTED())

def last_five():
    new = if_EXECUTED()[::-1]
    lis_new = sorted(new[:5], key=lambda data: data["date"])
    return lis_new[::-1]

#pprint(last_five())

def data_time(data):

    data = data.split("-")
    index_data_2 = [data[2][:2], data[1], data[0]]
        #the_data = datetime.strptime("-".join(index_data_2), "%d-%m-%Y")
    return ".".join(index_data_2)

#print(data_time("2019-07-12T20:41:47.882230"))

def organization_transfer(description):
    return description

#organization_transfer()

def number_cart_send(send):
    account_number = send.split(' ')[-1]
    if len(account_number) == 20:
        return f'Счет **{account_number[16:]}'
    else:
        return f'{" ".join(send.split(" ")[:-1])} ' \
               f'{account_number[0:4]} {account_number[4:6]}' \
               f'** **** {account_number[12:]}'

#print(number_cart_send("Visa Classic 6831982476737658"))

def number_cart_recipient(recipient):
    account_number = recipient.split(' ')[-1]
    if len(account_number) == 20:
        return f'Счет **{account_number[16:]}'
    else:
        return f'{" ".join(recipient.split(" ")[:-1])} ' \
               f'{account_number[0:4]} {account_number[4:6]}' \
               f'** **** {account_number[12:]}'

#score()

def money(amount_of_money, currency):
    return f'{amount_of_money} {currency}'

#print(money("97853.86", "руб."))