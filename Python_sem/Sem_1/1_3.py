# Напишите программу которая на вход принемает число N и выводит число от -N до N
print('Введждите число')
N = int(input())
for i in range(-N , N+1):
    print(i, end=" ")