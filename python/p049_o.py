from itertools import permutations
import pandas as pd
from dask import delayed, compute

#############################################
def isqrt(n: int) -> int:
    """
    Integer square root using Newton's method
    x² = n -> x² - n = 0
    Newton method f(x) = 0
    x_new = x - f(x)/f'(x)
    """
    if n < 2:
        return n
    x = n
    while True:
        x_new = (x + n // x) // 2
        if x_new >= x:
            return x
        x = x_new

def is_prime_v1(n: list) -> list:
    """Check if numbers in list are prime"""
    out = []
    for v in n:
        if v <= 1:
            continue
        elif v <= 3:
            out.append(v)
        elif v % 2 == 0:
            continue
        else:
            is_prime = True
            for i in range(3, isqrt(v) + 1, 2):
                if v % i == 0:
                    is_prime = False
                    break
            if is_prime:
                out.append(v)
    return out

perm_list_f = lambda s: ["".join(p) for p in permutations(s)]

def df_arithmetic_sequences(number_string: str) -> list:
    perm_list = perm_list_f(str(number_string))
    perm_list = list(set(perm_list))  # remove duplicates
    out = is_prime_v1([int(x) for x in perm_list if x[0] != '0'])
    
    if len(out) < 3:  # Need at least 3 primes for an arithmetic sequence
        return []
    
    # Find all 3-term arithmetic sequences
    primes = sorted(out)
    sequences = []
    n = len(primes)
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if primes[j] - primes[i] == primes[k] - primes[j]:
                    sequences.append([primes[i], primes[j], primes[k]])
    
    return sequences[0] if sequences else []

@delayed
def process(s: str):
    seq = df_arithmetic_sequences(s)
    if len(seq) == 3:
        return seq
    return None
##############################################
tasks = [process(str(s)) for s in range(1000, 10000)]
results = compute(*tasks)
# Filter out None results and print
print([r for r in results if r is not None])
unique = {tuple(seq) for seq in results if seq is not None}
unique_lists = [list(t) for t in unique]
print(unique_lists)

###############################################
###############################################

from typing import List
import math
def list_primality(n: int) -> List[bool]:
	# Sieve of Eratosthenes
	result: List[bool] = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(math.isqrt(n) + 1):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result

def compute():
	LIMIT = 10000
	isprime = list_primality(LIMIT - 1)
	print(isprime[:100]) 
	for base in range(1000, LIMIT):
		if isprime[base]:
			for step in range(1, LIMIT):
				a = base + step
				b = a + step
				if     a < LIMIT and isprime[a] and has_same_digits(a, base) \
					and b < LIMIT and isprime[b] and has_same_digits(b, base) \
					and (base != 1487 or a != 4817):
					return str(base) + str(a) + str(b)
	raise RuntimeError("Not found")


def has_same_digits(x, y):
	return sorted(str(x)) == sorted(str(y))
compute()