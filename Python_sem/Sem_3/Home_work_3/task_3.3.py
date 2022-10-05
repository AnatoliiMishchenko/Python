# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

def decimal_to_binary_conversion(number):
    if number >= 2:
        decimal_to_binary_conversion(number//2)
    print(number % 2, end="")


decimal_to_binary_conversion(int(input()))


def convert_binary(number):
    list_number = []

    while number > 0:
        list_number.insert(0, number % 2)
        number//=2

    print(*list_number, sep="")

print()

convert_binary(int(input()))