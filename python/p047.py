"""
# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 * 7
# 15 = 3 * 5
# The first three consecutive numbers to have two distinct prime factors are:
# 644 = 2^2 x 7 x 23
# 645 = 3 x 5 x 43
# 646 = 2 x 17 x 19
Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""
def prime_factorization_by_division(n):
    prime_factors = []
    c = 2
    while n > 1:
        if n % c == 0:
            prime_factors.append(c)
            while n % c == 0:
                n //= c
        else:
            c += 1
    return list(set(prime_factors))

def compute():
    for i in range(1000, 150000-3):
        args = [i+k for k in range(4)]
        prime_factors = all(len(prime_factorization_by_division(arg)) == 4 for arg in args)
        if prime_factors:
            return args[0]
    return None

if __name__ == "__main__":
    print('Project Euler 47')
    out = compute()
    print(out)
    
    