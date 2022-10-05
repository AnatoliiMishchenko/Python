# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# in
# 54
# out
# [2, 3, 3, 3]
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]
# in
# 650
# out
# [2, 5, 5, 13]

number = int(input(" Введите число "))

def del_number(number):
    list_simple = []
    delet = 2
    while number > 1:
        if number % delet == 0:
            list_simple.append(delet)
            number = number/delet
        else:
            delet += 1
    return list_simple


print(del_number(number))
