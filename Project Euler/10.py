import math  # noqa: INP001
import time
from functools import cache


@cache
def prime(n):
    if n % 2 == 0:
        return False
    sq = math.isqrt(n)
    for i in range(3, sq + 1, 2):  # noqa: SIM110
        if n % i == 0:
            return False
    return True


t0 = time.perf_counter()
i = 3
sum = 2  # noqa: A001
while i < 2_000_000:  # noqa: PLR2004
    if prime(i):
        sum += i  # noqa: A001
    i += 2
t1 = time.perf_counter()
print(sum, t1 - t0)
# 7.91391
# 7.70056
# 3.94768
