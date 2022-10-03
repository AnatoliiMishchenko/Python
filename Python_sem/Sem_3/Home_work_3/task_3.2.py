# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]


import random


def random_list(count: int):
    arr = [random.randint(0, count*2) for arr in range(count)]
    return arr


def product_of_pairs_of_numbers(list):
    long_new_list = int(len(list)/2)
    new_my_list = []
    for j in range(long_new_list):
        new_my_list.append((list[j]*list[len(list) - j-1]))
    if (len(list) % 2 == 0):
        new_my_list
    else:
        new_my_list.append((list[int(len(list)/2) ]))
    return new_my_list


my_list = random_list(int(input()))
print(my_list)

print(product_of_pairs_of_numbers(my_list))
