# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def neg_fib(number):
    a = 1 
    b = 1
    list_my = [0]

    for i in range(number):
        list_my.append(a)
        list_my.insert(0, a*(-1)**i)
        a, b = b, a+b
    return list_my


print(*neg_fib(int(input())))
