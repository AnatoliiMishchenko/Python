from read_data import *


def init():
    if not (len(read_data()) > 0):

        with open("name.csv", 'a+', encoding='utf - 8') as file:
            file.write("id;surname;name;class;status\n")

        with open("adress.csv", 'a+', encoding='utf - 8') as file:
            file.write("id;city;street;house;apartament; other\n")

        with open("class.csv", 'a+', encoding='utf - 8') as file:
            file.write("id;row;col\n")
