import numpy as np
import sys
def prime_factorization_by_division():
    n = int(sys.argv[1])
    prime_factors = []
    c = 2 # smallest prime number
    prime_factors.append(c)
    while(n > 1):
        if(n % c == 0):
            print(c, end=" ")
            n = n / c
            prime_factors.append(c) # only keep prime factors
        else:
            c = c + 1
            #prime_factors.append(c) # all factors
    maxF = max(np.array(prime_factors))
    return maxF
if __name__ == "__main__":
    print ('Project Euler 3')
    print (prime_factorization_by_division())