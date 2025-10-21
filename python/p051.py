# prime digit replacement
# searching for the tiniest prime that, when some of its digits are swapped out with the same digit, produces 8 different prime numbers. - “eight prime value family”
# ans 121313
#Find the smallest prime number where you can replace some of its digits 
# (they don’t have to be next to each other) with the same digit, 
# and this creates eight different prime numbers.
# If 56003 is a prime, and replacing the two 0s with the same digit gives other primes like 56113, 56223, …, up to 8 primes
from math import isqrt
# useful fucntinos
def is_prime_list(limit):
    limit = int(limit)
    "sieve_of_eratosthenes returns a list of true/false for primes <= limit"
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit+1, i):
                sieve[j] = False
    return  sieve 
########################################################################################
########################################################################################
def to_number(digits):
    result = 0
    for d in digits:
        # we miltiply by 10, shift all digits one place to the left(in base 10)
        # "room made" for one new digits can be added
        result = result*10 + d
    #result = int(''.join(map(str, digits)))
    return result
#bitmasking trick
def do_mask(digits,mask):
    """
    ~mask → bitwise NOT of mask
    mask in binary: 00001100 - ~mask flips all bits → 11110011
    (~mask >> i) & 1 → picks the i-th bit of the inverted mask
    Multiply d * bit → either keeps d (if bit is 1) or makes it 0 (if bit is 0)
    do_mask zeroes out digits where the mask bit is 1 and keeps digits where the mask bit is 0.
    """
    return [d * ((~mask >> i) & 1) for (i, d) in enumerate(digits)]
def add_mask(digits,mask):
    """
    digits = [5, 6, 6, 6, 3]
    mask = 0b01100  # decimal 12
    add_mask(digits, mask)  # → [5, 7, 7, 6, 3]
    mask >> i & 1 → picks the i-th bit of the mask (0 or 1)
    Add that bit to the digit d
    Result: a new list where digits corresponding to 1s in mask are incremented by 1
    """
    return [d + ((mask >> i) & 1) for (i, d) in enumerate(digits)]

#masked_part = do_mask(digits, mask)  # keeps digits where mask is 0
#added_part = add_mask(digits, mask)  # adds 1 to digits where mask is 1
# [5, 6, 6, 6, 3]  mask=12
# [d + ((mask >> i) & 1) for (i, d) in enumerate(n)] -> [5, 6, 7, 7, 3]
# [d * ((~mask >> i) & 1) for (i,d) in enumerate(n)] -> [5, 6, 0, 0, 3]

########################################################################################
########################################################################################

def compute():
    isprime = is_prime_list(1000000)
    for i in range(len(isprime)):
        if not isprime[i]:
            continue

        n = [int(c) for c in str(i)]
        for mask in range(1<<len(n)):
            digits = do_mask(n,mask)
            count = 0
            for j in range(10):
                if digits[0] != 0 and isprime[to_number(digits)]:
                    count +=1
                digits = add_mask(digits,mask)

            if count == 8:
                digits = do_mask(n,mask)
                for j in range(10):
                    if digits[0] != 0 and isprime[to_number(digits)]:
                        return str(to_number(digits))
                    digits = add_mask(digits,mask)
    raise AssertionError("Not found!")

if __name__ == "__main__":
    print(compute())
