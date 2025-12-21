def sum_for_list(lst):
    factors_set = set()
    for n in lst:
        temp = abs(n)
        i = 2
        while i * i <= temp:
            if temp % i == 0:
                factors_set.add(i)
                while temp % i == 0:
                    temp //= i
            i += 1
        if temp > 1:
            factors_set.add(temp)
            
​
    primes = sorted(list(factors_set))
    ans = []
    for p in primes:
        current_sum = 0
        for n in lst:
            if n % p == 0:
                current_sum += n
        ans.append([p, current_sum])
        
    return ans