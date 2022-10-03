# * 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15
print('Введите число челенов N')
N = int(input())
print('Введите положение первого числа')
one = int(input('Position one:'))
print('Введите положение второго числа')
two = int(input('Position two:'))
my_list = []

for i in range(-N, N+1):
    my_list.append(i)
print(my_list)

if((one > len(my_list) and two > len(my_list)) or (one <= 0 and two <= 0)):
    print('Таких позчий нет в списке')
elif(one > len(my_list) or two > len(my_list) or one <= 0 or two <= 0) :
    if( one > len(my_list) or one <= 0 ):
        print('Позиции под номером 1 нет в списке')
    elif(two > len(my_list) or two <= 0):
        print('Позиции под номером 2 нет в списке')
elif(one <= len(my_list) and two <= len(my_list)):
    print('Произведение позиций', {one}, 'и', {two}, ' = ', int(my_list[one-1]) * int(my_list[two-1]))
