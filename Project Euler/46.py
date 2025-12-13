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


s = set()
x = 35
flag = True
while flag:
    if not prime(x):
        for i in range(x):
            if prime(i):
                s.add(i)
