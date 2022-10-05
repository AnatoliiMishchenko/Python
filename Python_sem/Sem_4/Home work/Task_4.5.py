# 5. ** Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# in
# "poly.txt"
# "poly_2.txt"

# out
# The contents of the files do not match!

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
    

def mnogochlen(k):
    with open("my_txt1.txt", 'a', encoding="UTF-8") as t:
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
    k = int(input("Введите степень многочелена k2 "))
    mnogochlen(k)

open("file3.txt","w").write(open("my_txt1.txt","r").read() + open("my_txt.txt","r").read())