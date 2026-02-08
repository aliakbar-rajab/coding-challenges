def dont_give_me_five(start, end):
    def count(n):
        if n < 0: return 0
        s = str(n)
        length = len(s)
        total = 0
        for i, c in enumerate(s):
            digit = int(c)
            power = length - i - 1
            if digit < 5:
                total += digit * (9 ** power)
            elif digit == 5:
                total += digit * (9 ** power)
                return total
            else:
                total += (digit - 1) * (9 ** power)
        return total + 1
​
    if end < 0:
        return count(abs(start)) - count(abs(end) - 1)
        
    elif start >= 0:
        return count(end) - count(start - 1)
        
    else:
        return count(abs(start)) + count(end) - 1