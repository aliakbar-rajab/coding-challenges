def cir(n):
    lst = [n]
    for i in range(len(str(n)) - 1):
        lst.append(int(str(n)[-1] + str(str(n))[:-1]))
        n = int(str(n)[-1] + str(str(n))[:-1])
    return lst


def prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True


limit = 1_000_000
s = set()
for i in range(limit):
    k = i
    if k in s:
        pass
    elif prime(k):
        if len(str(k)) == 1:
            s.add(k)
        else:
            k = cir(k)
            if all(prime(m) for m in k):
                s.update(k)

print(len(s))
