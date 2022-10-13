# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import randint

count = int(input("Введите количество элементов "))


my_list = [randint(0, 50) for i in range(count)]


print(my_list)


m = [my_list[j+1] for j in range(len(my_list) - 1) if my_list[j+1] > my_list[j]]


print(m)
