a = 17
b = 8146798528947


def gcd(number1: int, number2: int):
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return number1


print(gcd(a, b))


import math

print(math.gcd(a,b))

