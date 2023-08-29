
import math, time
def binomial(n: int, k: int) -> int:
	assert 0 <= k <= n
	return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
def compute():
	return str(binomial(40, 20))

t1 = time.time()
out = compute()
t2 = time.time()
print (out,t2-t1)

def factorial(n):
    # Base case
    if n <= 1:
        return 1
    # Recursive step
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120
