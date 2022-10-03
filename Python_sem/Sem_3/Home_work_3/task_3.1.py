# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8

import random


def random_list(count: int):
    arr = [random.randint(0, count*2) for arr in range(count)]
    return arr


def summ_elements_not_even(list: list):
    sum = 0
    for i in range(0,len(list),2):
       # if (i % 2 == 0):
            sum += list[i]
    return sum


my_list = random_list(int(input()))
print(my_list)

print("сумма нечетных элементов = " + str(summ_elements_not_even(my_list)))
