#import numpy as np
import sys
# find Find the 10001st prime
def prime_factorization(n):
    prime_factors = []
    c = 2
    while(n > 1):
        if(n % c == 0):
            n = n / c
            prime_factors.append(c)
        else:
            c = c + 1
    if len(prime_factors)==1:
        return True
    else:
        return False

def check_primes():
    m = int(sys.argv[1])
    primes,i = [],0
    n = 2
    while (i<m):
        if prime_factorization(n):
            primes.append(n)
            i = i + 1
            n = n + 1
        else:
            n = n +1
    print (primes[-1])

        
if __name__ == "__main__":
    print ('Project Euler 3')
    print (check_primes())