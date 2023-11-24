p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
m = p * q
print(m)

#  d * e = 1 mod N


def gcdExtended(a, b):
    if a == 0 :
        return b,0,1
    gcd,x1,y1 = gcdExtended(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd,x,y


# m, a = map(int, input().split())
# gcd, x, y = gcdExtended(a, m)
gcd, x, y = gcdExtended(m, e)
if gcd == 1:
    print((x % m + m) % m)
else:
    print(-1)
