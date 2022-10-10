# 2. Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
from random import choices


def get_list(size):
    return choices(range(size*2), k=size)

def new_list(array):
    new_list = []
    for i in range(len(array)):
        some = array[i]
        arr = [some]
        for j in range(i+1, len(array)):
            if array[j] > some:
                arr.append(array[j])
                some = array[j]
        if len(arr) > 1:
            new_list.append(arr)
    return new_list

tt = get_list(10)

print(tt, new_list(tt), sep="\n") 
