# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27


print('Введте число')
number_my = input()
summ_number = 0

n = len(number_my)
count = int(float(number_my)*10**n)

while count:
    summ_number += int(count % 10)
    count = count/10
print(summ_number)
# Хотел сделать проверку про введенную строку через Try  но не сработало(((
