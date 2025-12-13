s1 = 0
s2 = 0
for a in range(1, 101):
    s1 += a**2
    s2 += a
print(s2**2 - s1)
