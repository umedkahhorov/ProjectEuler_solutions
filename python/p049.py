# prime permuatations
# 1487,4817,8147 (delta=3330): each are prime, permutations of one another
# 4 digits perm sequence
# [1487, 4817, 8147] [2969, 6299, 9629]
from itertools import permutations

###
number_string = "1487"
perm_list_v1 = [a+b+c+d for a in number_string for  b in number_string if b!=a for c in number_string if c not in (a,b) for d in number_string if d not in (a,b,c)]
###
perm_list_f =  lambda s: [a+b+c+d for a in s for b in s if b!=a for c in s if c not in(a,b) for d in s if d not in (a,b,c)]
perm_list_f = lambda s: ["".join(p) for p in permutations(s)]
perm_list_v2 = perm_list_f("1487")
###
#print(perm_list_v1)
#print(set(perm_list_v2)==set(perm_list_v1))
###
def isqrt(n: int) -> int:
    """
    x² = n  -> x² - n = 0 
    Newton method f(x) = 0
    x_new = x - f(x)/f'(x)
    """
    if n < 2: 
        return n
    x=n
    while True:
        x_new = (x + n//x)//2
        if x_new >=x: 
            return x
        x = x_new
###
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

def diff_matrix(n: list) -> list:
    """Calculate the difference between each pair of numbers in the list"""
    out = []
    for value in n:
        out.append([abs(value - x) for x in n])
    return out
		
def find_arithmetic_sequences(n: list) -> list:
    """Find arithmetic sequences in the list of prime numbers"""
    sequences = []
    primes = sorted(set(n))
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            a,b = primes[i], primes[j]
            c = b + (b - a)
            if c in primes:
                sequences.extend([a, b, c])
    return sequences

if __name__ == "__main__":

    for ilist in range(1000, 9999 + 1):
            perm_list = perm_list_f(str(ilist))
            out = is_prime_v1([int(x) for x in perm_list if x[0] != '0'])
            sequences = find_arithmetic_sequences(out)
            if len(sequences) == 3:
                print(f"Number: {ilist}, Prime permutations: {out}, Arithmetic sequences: {sequences}")


	
