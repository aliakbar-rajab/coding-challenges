# 1_2_3_4_5_6_7_8_9_0
x = 1010101030
step = 40
while True:
    z = x**2
    s = str(z)
    if (
        s[0] == "1"
        and s[2] == "2"
        and s[4] == "3"
        and s[6] == "4"
        and s[8] == "5"
        and s[10] == "6"
        and s[12] == "7"
        and s[14] == "8"
    ):
        print(x)
        break
    else:
        x += step
        step = 100 - step
