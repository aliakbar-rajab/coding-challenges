import time

dic = dict()


def f1(x):
    if x in dic:
        return dic[x]
    else:
        if x == 1:
            return 1
        if x == 2:
            return 2
        ans = f1(x - 1) + f1(x - 2)
        dic[x] = ans
        return ans


l = [1, 2]


# time = 2.179e-05
def f2(n):
    while len(l) < n:
        l.append(l[-1] + l[-2])
    return l[n - 1]


# x = 1
# total = 0
# t0 = time.perf_counter()
# while f2(x) < 4_000_000:  # call 1 (bloated on purpose)
#     if f2(x) % 2 == 0:  # call 2
#         total += f2(x)  # call 3
#     x += 1
# t1 = time.perf_counter()

# print(total, t1 - t0)

# AI time= 8.199e-06
limit = 4_000_000
a, b = 1, 2
total = 0
t0 = time.perf_counter()
while a < limit:
    if (a & 1) == 0:  # faster than % 2
        total += a
    a, b = b, a + b
t1 = time.perf_counter()
print(total, t1 - t0)
