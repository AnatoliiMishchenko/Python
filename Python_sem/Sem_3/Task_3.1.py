# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# # Напишите программу, которая определит, присутствует ли в заданном списке число,
# # полученное от пользователя.
from random import sample

def find_num(count, number):
    count = count if count > 0 else -count
    arr = sample(range(1,count*2), count)
    print(arr)
    if(number in arr):
        return True
    return False


print(find_num(10,5))