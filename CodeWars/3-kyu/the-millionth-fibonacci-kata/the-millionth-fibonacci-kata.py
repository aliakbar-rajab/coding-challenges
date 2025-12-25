def fib(n):
    m = abs(n)
​
    a, b = 0, 1
    for i in range(m.bit_length() - 1, -1, -1):
        c = a * (2*b - a)
        d = a*a + b*b
        if (m >> i) & 1 == 0:
            a, b = c, d
        else:
            a, b = d, c + d
​
    sign = -1 if (n < 0 and (m % 2 == 0)) else 1
    return sign * a
​