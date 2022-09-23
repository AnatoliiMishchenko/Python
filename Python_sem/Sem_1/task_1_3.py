# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# -------------------------------------- 1 вариант

num = int(input())

for i in range(-num, num + 1):
    print(i, end=", ")

# -------------------------------------- 2 вариант

num = int(input())
op_num = num + 1
step = 1
if num < 0:
    op_num = num - 1
    step = -1

for i in range(-num, op_num, step):
    print(i, end=", ")


# -------------------------------------- 3 вариант

num = int(input())
neg_num = -num
print(neg_num, end=", ")

while num != neg_num:
    if num > 0:
        neg_num += 1
    else:
        neg_num -= 1
    print(neg_num, end=", ")
