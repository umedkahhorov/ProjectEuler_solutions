# Even Fibonacci numbers
import numpy as np
import time

def fibonacci_sum(n):
    """
    sum even Fibonacci numbers
    """
    ans = 0
    x = 1
    y = 2
    while x<=n:
        if x%2==0:
            ans +=x 
        x,y = y,x+y
    return ans
def fibonacci_sum2(n):
    """
    sum even Fibonacci numbers up to n using dynamic programming
    """
    ans = 0
    fib = [0,1,2]
    while fib[-1]<=n:
        if fib[-1]%2 ==0:
            ans +=fib[-1]
        fib.append(fib[-1] + fib[-2])
    return ans
n = int(4e6)
if __name__ == "__main__":
    print ('Project Euler 1')
    t1 = time.time()
    out = fibonacci_sum(int(4e+6))
    t2  = time.time()
    print (out,t2-t1)

    t1 = time.time()
    out = fibonacci_sum2(int(4e+6))
    t2  = time.time()
    print (out,t2-t1)

