# recursion - one doll has within in a small doll, solve problem bu solving smaller instance of the sam eproblem, unless its soo small to solve it directly
# factorial n! 5! product of int from 1 to n, 5  = 1 x 2 x 3 x 4 x 5 
# number of combinations of 'n' objects taken 'r' C(n,r)
# ans 4075
import time
from math import factorial

def get_factorial(n):
    # base case
    if n <= 1:
        return 1
    # recursive step
    else:
        return n * get_factorial(n-1)

def get_binomial(n: int, r: int) -> int:
	assert 0 <= r <= n
	return factorial(n) // (factorial(r) * factorial(n - r))

def compute():
    res = 0
    for n in range(23,101):
        for r in range(1,n+1):
            C = get_binomial(n,r)
            if C >= 1e6:
                res +=1
    return res

# option 2
#ans = sum(1 for n in range(23,101) for r in range(1,n+1) if get_binomial(n,r) >=1e6)

    


if __name__ == "__main__":
    print(get_factorial(5))
    print(get_binomial(23,11))
    t1 = time.time()
    print(compute())
    t2 = time.time()
    print (t2-t1)
    t1 = time.time()
    ans = sum(1 for n in range(23,101) for r in range(1,n+1) if get_binomial(n,r) >=1e6)
    print(ans)
    t2 = time.time()
    print (t2-t1)
