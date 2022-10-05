# 1. Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

from audioop import minmax


def checking_str(count):
    arr = count.split()
    for i in arr:
        if not i.strip("-").isdigit():
            return []
    return arr


def max_min_number(arrya):
    if arrya:
        return min(arrya, key=int), max(arrya, key=int)
    return []


list = (checking_str(input("введите числа списка ")))
print(list)
print(max_min_number(list))
