# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988
from decimal import ROUND_HALF_DOWN,  Decimal


number = (input(" введите число "))
accuracy_number = (input(" введите точность например 0,01 (это два знака) "))

def number_accuracy (number , accuracy_number):
    number_accuracy = Decimal(number).quantize(Decimal(accuracy_number), ROUND_HALF_DOWN)
    return number_accuracy

print(number_accuracy(number,accuracy_number))


