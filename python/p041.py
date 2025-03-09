# Pandigital Prime 2143 
# What is the largest n-digit pandigital prime - 7652413
# any pandigital number that uses 8 or 9 digits (i.e. the digits 1–8 or 1–9) will have a digit sum that is divisible by 3
# So, there’s no need to search for pandigital primes with 8 or 9 digits—only up to 7-digit pandigital numbers might yield a prime.

from math import isqrt
from itertools import count
def prime_check(n: int) -> bool:
    if n <=1:
        return False
    elif n<=3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3,isqrt(n)+1,2):
            if n % i == 0:
                return False
        return True

def ispandigital(n):
    # simply check if the digits of n are exactly "1" to len(n)
    s = str(n)
    if set(s)==set("123456789"[:len(s)]):
        return n
    else:
        return 0
        




if __name__ =="__main__":
    n = 2143
    print(prime_check(n))
    print(ispandigital(n))
    print(max(n for n in range(1,10**7) if ispandigital(n) and prime_check(n)))