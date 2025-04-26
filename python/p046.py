# A composite number is a positive integer greater than 1 that has at least one positive divisor other than 1 and itself. Equivalently, it can be “built” by multiplying two smaller positive integers.
#  odd composites factor into odd primes.
# 9=3*3
# 15=3*5
# 21=3*7
## Goldbach's Other Conjecture:
### Prime
# A prime is a whole number greater than 1 whose only divisors are 1 and itself
# Square
# A square is the result of multiplying an integer by itself 1² = 1
# “Twice a square” just means you take one of those squares and multiply it by 2×1² = 2
# the sum of a prime and twice a square p + 2·n²
from itertools import filterfalse, dropwhile, count

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit+1, i):
                sieve[j] = False
    return  sieve 
    #return [i for i, prime in enumerate(sieve) if prime]


def compute(N):
    """
    to decide whether a given odd int N (odd composite number):
    N = p + 2*n²
    one prime number p, and
    one integer n, form its square n², double that to 2·n²,
    """
    # list of prime booleans
    primes = sieve_of_eratosthenes(N)
    # the largest n need to try
    max_n = int((N/2)**0.5)
    for n in range(1, max_n+1):
        p = N - 2*n*n
        if p>1 and primes[p]:
            # found odd composite N=p+2*n²
            return n, p
    return None

def canbe_written(odd_composite):
    """
    Return True if odd_composite = p + 2*n^2 for some prime p and n >= 1.
    Uses global `isprime` function for primality checks.
    """
    for double_square in (2 * n * n for n in count(1)):
        p = odd_composite - double_square
        if p < 0:
            break
        if isprime(p):
            return True
    return False



if __name__ == "__main__":
    limit = 10000
    primes = sieve_of_eratosthenes(limit)
    print(f"Primes up to {limit}: {primes}")
    N = 10000
 # Test the decomposition for several values of N
    for N in range(3,limit,2):
        if not primes[N]:
            # N is an odd composite number
            result = compute(N)
            if result:
                pass
                #n, p = result
                #print(f"{N} = {p} + 2*{n}^2")
            else:
                print(f"No representation for N={N} as prime + 2*n^2")
    # Upper bound for search
    limit = 10000

    # Precompute prime flags up to limit
    prime_flags = sieve_of_eratosthenes(limit)
    def isprime(x):
        return prime_flags[x] if 0 <= x <= limit else False

    # Generate odd composites starting at 9
    odd_composites = filterfalse(isprime, range(9, limit, 2))

    # Find and print the first odd composite that fails the representation
    result = next(dropwhile(canbe_written, odd_composites))
    print(result)
