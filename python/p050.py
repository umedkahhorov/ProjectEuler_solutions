# Consecutive Prime Sum 41 = 2 + 3 + 5 + 7 + 11 + 13
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
# compute(1000000) = 997651
######################################################################
from math import isqrt
def get_prime_list(limit):
    "sieve_of_eratosthenes returns a list of primes <= limit"
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, isqrt(limit) + 1):
        if sieve[i]:
            for j in range(i*i, limit+1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]
def is_prime(limit):
    "sieve_of_eratosthenes returns a list of true/false for primes <= limit"
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit+1, i):
                sieve[j] = False
    return  sieve 
######################################################################
def compute(limit):
    ans = 0
    primes = get_prime_list(limit)
    is_prime_list = is_prime(limit)
    # sonsecutive prime sum: 41 = 2 + 3 + 5 + 7 + 11 + 13
    consecutive_ps = 0
    # outer loop over all primes
    for i in range(len(primes)):
        sum_p = primes[i] # start with the current prime
        consec = 1
        # inner loop to add consecutive primes, shifted from the outer loop
        for j in range(i+1,len(primes)):
            sum_p += primes[j] # add priems from i to ...
            consec += 1
            if sum_p >= len(is_prime_list):
                break
            if is_prime_list[sum_p] and consec > consecutive_ps:
                ans = sum_p
                consecutive_ps = consec
    return ans
