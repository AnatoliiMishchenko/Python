# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке
# либо сообщит, что её нет.
from random import choices


def name_random(count, number):
    my_list = []
    for i in range(count):
        nan = choices(number, k=3)
        my_list.append("".join(nan))
    return my_list


my_list = name_random(10, "xyz")
print(my_list)


def find_count(word, list: list):
    if word in list and list.count(word) > 1:
        index = list.index(word)
        print(list.index(word, index+1))
    else:
        print(-1)


find_count(input(), my_list)
