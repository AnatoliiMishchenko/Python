# 3. Задайте два числа. Напишите программу, которая найдёт
# НОК (наименьшее общее кратное) этих двух чисел.
from math import gcd

A = int(input("Введите число А "))
B = int(input("Введите число B "))


def NOK_A_B(A, B):
    result = (A*B)//gcd(A, B)
    return result

print(NOK_A_B(A,B))
