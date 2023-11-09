
def factorial(n):
    dp = [1] * (n+1)

    for i in range(1,n+1):
        dp[i] = dp[i-1]*i
    return dp[n]

if __name__ == "__main__":
    print (factorial(10))
    ans = str(factorial(100))
    out = 0
    for n in ans:
        out +=int(n)
    print (out)
