p = int(input("Введите p: "))
q = int(input("Введите q: "))
e = int(input("Введите e: "))
n = (p-1)*(q-1)

try:
    d = pow(e, -1, n)
    print("Секретный ключ d: ", d)
    print("N: ", n)
except(e):
    print(e)




