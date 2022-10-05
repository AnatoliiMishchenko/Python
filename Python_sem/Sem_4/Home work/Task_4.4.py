# 4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

# in
# 0
# -1
# 4

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

from random import randint
import random





def mnogochlen(k):
    with open("my_txt.txt", 'a', encoding="UTF-8") as t:
        for i in range(k, -1, -1):
            char_l = "+-"
            B = random.choice(char_l)
            A = random.randrange(0,10)
            if A != 0:
                if i == 0:
                    t.write(f"{A} = 0 \n")
                else:
                    t.write(f"{A}*x^{i} {B}  ")
            else:
                if i == 0:
                    t.write(" = 0\n")
                


for i in range(3):
    k = int(input("Введите степень многочелена k "))
    mnogochlen(k)
   
   