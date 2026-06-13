# Dynamic Programming

# Sacrifice Memory for speed
# 2 types: Memoization and Tabulation

n = 50
c = 0
dp = [0] * (n + 1)

def fun(n, dp):    
    if n <= 1:
        return n

    global c
    c += 1

    if dp[n] != 0:
        return dp[n]
    
    dp[n] = fun(n - 1, dp) + fun(n - 2, dp)
    return dp[n]

print(f"Fib({n}) = {fun(n, dp)} \nc = {c}")