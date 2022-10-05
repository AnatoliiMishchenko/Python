# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!
# []
# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]


import random


number = int(input(" Введите количество элементов последовательнотси "))


def random_list(count):
    if (count < 0):
        print("Вы ввели отрицательное значение элементов")
        # return []

    arr = [random.randint(0, count) for arr in range(count)]
    return arr


my_list = random_list(number)


def unique_numbers(list):
    j = 0
    new_l = []
    for i in list:
        if i not in new_l:
            new_l.append(i)

    my_liss = []
    for i in new_l:
        count = 0
        for j in list:
            if i == j:
                count += 1
        if count <= 1:
            my_liss.append(i)

    return my_liss


print(my_list)

print(unique_numbers(my_list))
