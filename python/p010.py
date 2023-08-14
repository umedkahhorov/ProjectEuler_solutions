from eulerlib import if_prime,isPrime
import math
import time
import array
# sol 1
def compute1():
    t1 = time.time()
    x=2000000
    ans = 0
    for i in range(x):
        if if_prime(i):
            ans = ans + i
    t2 = time.time()
    print(t2-t1)
    return ans
# sol 2
def compute(lim):
    t1 = time.time()
    ans = 5
    n=5
    while n<=lim:
        if isPrime(n):
            ans = ans +n
        n = n +2
        if n<=lim and isPrime(n):
            ans = ans + n
        n = n+4
    t2 = time.time()
    print(t2-t1)
    #print (ans)
    return ans
# sol 3
def compute_sieve(lim):
    t1 = time.time()
    crosslim = abs(math.sqrt(lim))
    #print (crosslim)
    sieve = [False for i in range(2,lim)]
    #print (len(sieve))
    for n in range(4,lim,2):
        try:
            sieve[n]=True
        except IndexError:
            pass
            #print(n)
    for n in range(3,int(crosslim),2):
        if not sieve[n]:
            for m in range(int(n*n),lim-1,int(2*n)):
                try:
                    sieve[m]=True
                except IndexError:
                    #print (m)
                    pass
    sum =0
    for n in range(2,lim-1):
        try:
            if not sieve[n]:
                sum = sum+n
        except IndexError:
            #print (n)
            pass
    t2 = time.time()
    print(t2-t1)
    return sum
# sol 4
def sieve_of_eratosthenes(limit):
    sievebound = (limit - 1) // 2
    sieve = [False] * (sievebound + 1)
    crosslimit = (int(limit**0.5) - 1) // 2

    for i in range(1, crosslimit + 1):
        if not sieve[i]:
            for j in range(2 * i * (i + 1), sievebound + 1, 2 * i + 1):
                sieve[j] = True

    sum = 2  # 2 is prime

    for i in range(1, sievebound + 1):
        if not sieve[i]:
            sum += 2 * i + 1

    return sum
# sol 5
def sieve_of_eratosthenes2(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False

    sum_primes = sum(i for i, is_prime in enumerate(sieve) if is_prime)
    return sum_primes

limit = 2000000



if __name__ == "__main__":
    print ('Project Euler 3')
    print (compute1())
    #print (compute(2000000))
    #print (isPrime(3))
    print (compute_sieve(2000000))
    print ('Project Euler 3')
    limit = 2000000
    start_time = time.time()
    result = sieve_of_eratosthenes2(limit)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Sum of primes:", result)
    print("Execution time:", execution_time, "seconds")