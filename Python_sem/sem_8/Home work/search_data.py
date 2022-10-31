from print_data import *
from read_data import *


def search_data(word, data):
    if len(data) > 0:
        lst = []
        for item in data:
            if word in item:
                lst.append(item)
        if lst == []:
            return None
        else:
            return lst
    else:
        return None