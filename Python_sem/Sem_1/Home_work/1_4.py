# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*
# - 3
# - 6
# - 2
# - 1

print(' Введите значение четверти')
n = int(input())

if (n == 1):
    print('x > 0 and y > 0')
elif (n == 2):
    print('x < 0 and y > 0')
elif (n == 3):
    print('x < 0 and y < 0')
elif (n == 4):
    print('x > 0 and y < 0')
else:
    print('такой четверти не существует в двумерной оси координат')