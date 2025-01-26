# truncatable primes
# 3797 -> remove digits from left to right -> 3797, 797, 97, 7
# same from left to right
# sum of 11 primes
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

def compute():
    # 1) Generate primes up to some reasonable limit (e.g. 1,000,000)
    #    so we can find the 11 truncatable primes. You can adjust the limit
    #    if you’re sure 10,001 is sufficient, but typically a higher range is used.
    limit = 1000000
    primes_list = get_primes_up_to(limit)
    primes_set = set(primes_list)

    result = 0
    found_count = 0

    for prime in primes_list:
        # Usually, single-digit primes (2, 3, 5, 7) are not considered
        # "truncatable" by convention, so we skip them:
        if prime < 10:
            continue
        p_str = str(prime)
        # 3) Build all left-to-right truncations
        left_truncs = [int(p_str[i:]) for i in range(len(p_str))]

        # 4) Build all right-to-left truncations
        right_truncs = [int(p_str[:i]) for i in range(1, len(p_str) + 1)]

        # 5) Check if *all* truncations are prime
        #    (both left and right)
        if (all(t in primes_set for t in left_truncs)
            and all(t in primes_set for t in right_truncs)):
            result += prime
            found_count += 1
            print (prime)

            # 6) Stop once we've found 11 such primes (per Project Euler #37)
            if found_count == 12:
                break

    print(result)
    return result

def compute():
	ans = sum(itertools.islice(filter(is_truncatable_prime, itertools.count(10)), 11))
	return str(ans)


def is_truncatable_prime(n):
	# Test if left-truncatable
	i = 10
	while i <= n:
		if not eulerlib.is_prime(n % i):
			return False
		i *= 10
	
	# Test if right-truncatable
	while n > 0:
		if not eulerlib.is_prime(n):
			return False
		n //= 10
	return True

if __name__ == "__main__":
    out1 = sieve_of_eratosthenes(101)
    print (out1)
    out2 = get_primes_up_to(101)
    print (out2)
    compute()
