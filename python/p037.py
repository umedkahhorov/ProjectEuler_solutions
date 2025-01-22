def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit+1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

def get_primes_up_to(limit):
    """
    Return a list of all primes from 2 up to `limit` (inclusive),
    using naive factorization to check primality.
    NOTE: This method is fine for small limits but can be very slow for large limits.
    """
    primes = []
    for n in range(2, limit + 1):
        # Check if n is prime by naive factorization:
        temp = n
        divisor = 2
        factors = []
        
        while temp > 1:
            if temp % divisor == 0:
                temp //= divisor
                factors.append(divisor)
            else:
                divisor += 1
        
        if len(factors) == 1:  # Only one factor => n is prime
            primes.append(n)
    
    return primes
