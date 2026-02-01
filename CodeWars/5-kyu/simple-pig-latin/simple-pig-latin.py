def pig_it(text):
    t = text.split(' ') 
    res = []
    for i in t:
        if i.isalpha():
            f = i[0]
            g = i[1:]
            h = g + f + 'ay'
            res.append(h)
        else:
            res.append(i)
    return " ".join(res)