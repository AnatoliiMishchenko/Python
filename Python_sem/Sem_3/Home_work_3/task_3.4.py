# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

from random import uniform


def random_list(count):
    list_number = []
    if count <= 0:
        print("Вы ввели отрицательное значения элементов или 0")
        return [0, 0]

    for i in range(count):
        list_number.append(round(uniform(1, count), 2))
    return list_number


def dif_max_min(list):
    number_max = number_min = list[0] % 1

    for i in range(1, len(list)):
        number = round(list[i] % 1, 2)
        if number > number_max:
            number_max = number
        elif number < number_min:
            number_min = number

    result = round(number_max-number_min,2)
    print(f'Min: {number_min}, Max: {number_max}. Difference: {result}')
    return result


lisl_new = random_list(int(input("введите количество элементов ")))
print((lisl_new))
print(dif_max_min(lisl_new))
