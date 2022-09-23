# Напишите программу . которая на вход принемает 5 чисел и находит максимальное из низ.
max = 0
for i in range(5):
    print('Введите число')
    a = int(input())
    if max < a:
        max = a
print('max =', max)
