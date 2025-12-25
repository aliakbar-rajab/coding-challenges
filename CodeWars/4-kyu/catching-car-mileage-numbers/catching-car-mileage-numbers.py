def is_interesting(n, awesome_phrases):
    def check(num):
        if num < 100:
            return False
        s = str(num)
        if num in awesome_phrases:
            return True
        if int(s[1:]) == 0:
            return True
        if all(c == s[0] for c in s):
            return True
        if s in "1234567890":
            return True
        if s in "9876543210":
            return True
        if s == s[::-1]:
            return True
        return False
    if check(n):
        return 2
    if check(n + 1) or check(n + 2):
        return 1
    return 0