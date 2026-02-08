import re
def solve_runes(expression):
    match = re.match(r"(-?[\d?]+)([*+\-])(-?[\d?]+)=(-?[\d?]+)", expression)
    if not match:
        return -1
    term1, op, term2, result = match.groups()
    for i in range(10):
        digit = str(i)
        if digit in expression:
            continue
        t1_str = term1.replace('?', digit)
        t2_str = term2.replace('?', digit)
        res_str = result.replace('?', digit)
        candidates = [t1_str, t2_str, res_str]
        if any((len(n) > 1 and n.startswith('0')) or n.startswith('-0') for n in candidates):
            continue
        v1, v2, v_res = int(t1_str), int(t2_str), int(res_str)
        if op == '+' and v1 + v2 == v_res: return i
        if op == '-' and v1 - v2 == v_res: return i
        if op == '*' and v1 * v2 == v_res: return i
    return -1