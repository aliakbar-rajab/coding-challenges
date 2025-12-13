s = "0"
x = 1
while len(s) <= 1_000_000:
    s = s + str(x)
    x += 1
d = (
    int(s[1])
    * int(s[10])
    * int(s[100])
    * int(s[1000])
    * int(s[10000])
    * int(s[100000])
    * int(s[1000000])
)
print(d)
