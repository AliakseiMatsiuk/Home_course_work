from jeson_file import result
#from datetime import datetime
from pprint import pprint

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
    return "-".join(index_data_2)

#print(data_time())

def organization_transfer(description):
    return description

#organization_transfer()

def cart(cart):
    return cart

cart()







