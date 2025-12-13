from functools import cache


@cache
def fac(n):
    return 1 if n == 1 else n * fac(n - 1)


print(sum(map(int, str(fac(100)))))
