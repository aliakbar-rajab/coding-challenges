import time

t0 = time.perf_counter()


def prime(n):
    if n == 2:
        return True
    else:
        for i in range(3, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True


count = 0
i = 2
while count < 10001:
    if prime(i):
        count += 1
    i += 1
t1 = time.perf_counter()
print(t1 - t0)
# time: 0.943685
# time: 0.894417
# 0.087578
