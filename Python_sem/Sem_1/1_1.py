# Напишите программу. которая на вход принемает на вход два числа  и проверяет . является ли одно число квадратом другого

print('Введите число а')
a = int(input())
print('Введите число b')
b = int(input())
if (a == b**2 or b == a**2):
    print('число являпется квадратом другого')
else:
    print('число не являпется квадратом другого')

