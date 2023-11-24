import math

p = 8146798528947
q = 17


def extended_gcd(number1, number2):
    x, xx, y, yy = 1, 0, 0, 1
    while number2:
        q = number1 // number2
        number1, number2 = number2, number1 % number2
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return x, y, number1
# number1 = gcd(p,q)
# x*p + y*q = gcd(p,q)


print("(u, v, gcd(p,q)) = ", extended_gcd(p, q))
print("gcd(p,q) = ", math.gcd(p, q))
m = 517 // 17  # Сколько раз целое влазит
n = math.pow(7, 16) % 17  # Остаток от деления
print("m: = ", m)
print("n: = ", n)

a = 3
p = 13
print(pow(a,p-2) % p)
