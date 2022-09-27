# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

print('Введите число челенов N')
N = int(input())
my_list = []
summ_lisl = 0
for i in range(1, N+1):
    my_list.append(round((1+1/i)**i))
    summ_lisl += round((1+1/i)**i)
print(my_list, ' ->', summ_lisl)

