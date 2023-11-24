p = 28151


def order(g, p):
    for n in range(2, p):
        if pow(g, n, p) == g:
            print("g: ", g)
            print("n: ", n)
            return n
    return p


for g in range(2, p):
    o = order(g, p)
    if o == p:
        print(f"{g=} is a generator")
        break
