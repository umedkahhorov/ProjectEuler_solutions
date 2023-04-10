# Even Fibonacci numbers
import numpy as np

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
if __name__ == "__main__":
    print ('Project Euler 1')
    print (fibonacci_sum(int(4e+6)))