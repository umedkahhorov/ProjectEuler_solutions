import numpy as np
import time 
import math

def triangle_nth(n):
    sum = n * (n+1) / 2
    return int(sum)

def list_factors_1(n):
    factors = [i for i in range(1,n+1) if n%i==0]
    return len(factors)

def list_factors_2(n):
    factors = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            factors.add(i)
            factors.add(n//i)
    return len(factors)

if __name__ == "__main__":
    correct_answer = 227750
    t1 = time.time()
    #n_sum = triangle_nth(correct_answer)
    ans = list_factors_2(28)
    t2 = time.time()
    print (ans,t2-t1)