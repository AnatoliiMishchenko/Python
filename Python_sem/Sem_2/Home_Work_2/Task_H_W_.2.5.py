# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
import random


print(' Введите количество элеменктов списка')
count = int(input())
my_list = []
for i in range(count):
    my_list.append(i)
print(my_list)

for i in range(len(my_list)):
    index_random = random.randrange(0, (len(my_list)-1))
    my_list[i], my_list[index_random] = my_list[index_random], my_list[i]
print(my_list)
