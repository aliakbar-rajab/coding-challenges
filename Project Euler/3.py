import time

t0 = time.perf_counter()
n = 600851475143
f = 3
while f**2 < n:
    while n % f == 0:
        n /= f
    f += 2
t1 = time.perf_counter()
print(n, t1 - t0)
# 0.00083
# optimized after removing is_prime(): 0.00016     80% faster
