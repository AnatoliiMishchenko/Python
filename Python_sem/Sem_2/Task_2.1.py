print('Введите число челенов N')
N = int(input())

for i in range(N):
    result = -3
    result = result**i
    print(result, end=" ")
print('\n')

number = 1
for i in range(N):
    print(number, end=" ")
    number*=-3
   
