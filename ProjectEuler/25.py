from functools import cache


@cache
def fib(n):
    return 1 if n in {1, 2} else fib(n - 1) + fib(n - 2)


n = 3
while len(str(fib(n))) < 1000:  # noqa: PLR2004
    n += 1
print(n)


# AI
# An iterative approach is more efficient and avoids recursion limits.
# a, b = 1, 1  # F_1, F_2
# n = 2        # Start with the index of the second term 'b'

# while len(str(b)) < 1000:
#     # This is the classic, pythonic way to advance the sequence
#     a, b = b, a + b
#     n += 1

# print(n)
