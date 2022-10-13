# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100

# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

# in
# 424

# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147,
# 160, 168, 180, 189, 200, 210, 220, 231, 240, 252, 260, 273, 280,
# 294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]


import random

count = int(input("Введите количество элементов "))


# my_list = [i for i in range(20, count+1)]
# print(my_list)
# print()
# my_list_20_21 = [my_list[j] for j in range(len(my_list)) if (my_list[j] % 20 == 0 or my_list[j] % 21 == 0)]


my_list = list(filter( lambda x : not(x % 20  and x % 21) , [i for i in range(20, count+1)]))

print(my_list)
