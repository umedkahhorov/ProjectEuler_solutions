# prime digit replacement
# searching for the tiniest prime that, when some of its digits are swapped out with the same digit, produces 8 different prime numbers. - “eight prime value family”
from math import isqrt
from eulerlib import get_prime_list
from eulerlib import is_prime_list

def compute():
    plist = get_prime_list(100)
    plist = [i for i in plist if i>=10 and str(i)[-1]=="3"]
    print(plist)

if __name__ == "__main__":
    plist = get_prime_list(100)
    compute()
    print(plist)
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
def is_prime_list(limit):
    "sieve_of_eratosthenes returns a list of true/false for primes <= limit"
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit+1, i):
                sieve[j] = False
    return  sieve 
def filter_by_digits(plist,ndigit):
    # filter(function, iterable) 
    func = lambda n: len(str(n)) == ndigit
    filtered_plist = list(filter(func,plist))
    return filtered_plist


if __name__ == "__main__":
    plist = get_prime_list(99999)
    plist = filter_by_digits(plist,5)
    f_replace_digit = lambda p,i,n: p[:i] + str(n) + p[i+1:]
    print(plist)
