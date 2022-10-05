# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
# с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
# Уравнения и корни запишите в файл.

from math import sqrt


def sqrt_count(A, B, C):
    d = B**2 - 4 * A*C
    with open("result.txt", 'a', encoding="UTF-8") as my_f:
        my_f.write(f"{A}x^2 + {B}x + {C} = 0\n")
        if d > 0 and A:
            my_f.write(str((-B + sqrt(d))/(2*A))+"\n")
            my_f.write(str((-B - sqrt(d))/(2*A)) + "\n")

        elif d == 0 and B:

            my_f.write(str(-B/(2*A)) + "\n")

        else:
            my_f.write("Нет корней"+ "\n")


# for i in range(3):
sqrt_count(int(input("A ")), int(input("B ")),int(input("C ")))

