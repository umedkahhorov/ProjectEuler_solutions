import numpy as np
import sys
"""
What is the largest prime factor of the number
A prime number is a number that:
    Is greater than 1
    Can only be divided evenly by 1 and itself
Prime factors of a number
    prime numbers that, when multiplied together, give you the original number.
"""
def prime_factorization_by_division():
    n = int(sys.argv[1])
    prime_factors = []
    c = 2 # smallest prime number
    prime_factors.append(c)
    while(n > 1):
        if(n % c == 0):
            #print(c, end=" ")
            n = n / c
            prime_factors.append(c) # only keep prime factors
        else:
            c = c + 1
            #prime_factors.append(c) # all factors
    #maxF = max(np.array(prime_factors))
    return list(set(prime_factors))
if __name__ == "__main__":
    print ('Project Euler 3')
    a = prime_factorization_by_division()
    print (a)
    #print (a)
