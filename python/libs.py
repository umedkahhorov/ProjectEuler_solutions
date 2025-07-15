# Tests whether the given integer is a prime number.
import math
def is_prime(x: int) -> bool:
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, math.isqrt(x) + 1, 2):
			if x % i == 0:
				return False
		return True


def sieve_of_eratosthenes(limit):
   """
    Find all prime numbers up to a given limit using the Sieve of Eratosthenes.

    Theory (explained simply):
    - A prime number is a number greater than 1 that has no divisors other than 1 and itself.
    - The Sieve of Eratosthenes is a smart way to find all primes up to a certain number.
    - Imagine you have a list of numbers from 2 up to your limit.
    - Start with the first number (2). It's prime! Now, cross out all multiples of 2 (i.e., 4, 6, 8, ...) because they're not prime.
    - Move to the next number that isn't crossed out (3). It's also prime! Cross out all multiples of 3 (i.e., 6, 9, 12, ...).
    - Keep repeating this for the next uncrossed number, and so on.
    - When you've checked all numbers up to the square root of your limit, the numbers that aren't crossed out are all the primes.

    Args:
        limit (int): The upper limit to find primes (inclusive).

    Returns:
        list: A list of all prime numbers up to 'limit'.
    """
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit+1, i):
                sieve[j] = False
    return  sieve 
    #return [i for i, prime in enumerate(sieve) if prime]
	
