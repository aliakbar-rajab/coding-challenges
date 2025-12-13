import time

t0 = time.perf_counter()


def divisble(num):
    for n in range(2, 21):
        if num % n != 0:
            return False
    return True


# i = 20
# while not divisble(i):
#     i += 1
# t1 = time.perf_counter()
# print(i, t1 - t0)
# time: 68.93262840000534

# refactored
i = 40
while not divisble(i):
    i += 20
t1 = time.perf_counter()
print(i, t1 - t0)
# time: 3.5807222000003094
