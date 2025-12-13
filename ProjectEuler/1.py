# <p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
# <p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>
import numpy as np
import time


def f1():
    # 0.00025070000265259296
    lst = []
    for i in range(3, 1000):
        if i % 3 == 0 or i % 5 == 0:
            lst.append(i)

    l = np.array(lst)
    print(l.sum())


def f2():
    # 0.00014990000636316836
    sum = 0
    for i in range(3, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)


# AI
def f3(limit):
    # 1. Create an array of all numbers
    numbers = np.arange(1, limit)

    # 2. Create a boolean mask for the condition.
    # The '|' is the element-wise 'OR' operator for NumPy arrays.
    mask = (numbers % 3 == 0) | (numbers % 5 == 0)

    # 3. Use the mask to select the numbers and then sum them.
    # NumPy does all this work in optimized C code.
    return numbers[mask].sum()


start = time.perf_counter()
f3(1000)
end = time.perf_counter()
t = end - start
print(t)
