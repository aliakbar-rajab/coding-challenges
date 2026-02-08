def seq(n: int) -> int:
    MOD = 1_000_003
    current_sum = (n * (n + 1)) // 2
    current_sum %= MOD
    M = n
    for _ in range(n - 1):
        if (M - 1) % MOD == 0:
            multiplier = (n * (n + 1)) // 2
            current_sum = (current_sum * multiplier) % MOD
        else:
            inv = pow(M - 1, MOD - 2, MOD)
            term1 = (M * (pow(M, n, MOD) - 1) * inv) % MOD
            term_bracket = (term1 - n) % MOD
            current_sum = (current_sum * inv * term_bracket) % MOD
        M = (M * n) % MOD
    return current_sum