"""
ans = 45228
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 
5-digit number,15234,is1 through 5 pandigital. The product 7254 is unusual, as the identity, 39 x186=7254, containing multiplicand, multiplier, and product is 
 through pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital. 
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
Multiplicand x Multiplier = Product
     5        x     3     =   15
"""
from itertools import chain, combinations, permutations
import math
def check_pandigital(multiplicand, multiplier, product):
    digits = [int(d) for d in str(multiplicand) + str(multiplier) + str(product)]
    return len(digits) == 9 and len(set(digits)) == 9

# all_combinations = ["".join(map(str,combo)) for combo in combinations(elements,n)]
# all_combinations = [int("".join(map(str,combo))) for combo in chain(*[combinations(elements,r) for r in range(1,len(elements)+1) ] )]
#elements = list(range(1,10))
#n = len(elements)
#all_combinations = ["".join(map(str,perm)) for r in range(1,n+1) for perm in permutations(elements,r)]

def compute():
     res = []
     elements = list(range(1,10))
     all_permutations = ["".join(map(str,perm)) for perm in permutations(elements)]
     print (len(all_permutations),all_permutations[0])
     for v in all_permutations:
          for i in range(1,len(v)-1):
               for j in range(i+1,len(v)-i +1):
                    multiplicand = int(v[:i])
                    multiplier = int(v[i:j])
                    product = int(v[j:])
                    if multiplicand * multiplier == product:
                         res.append(product)
     return res
def compute_v2():
     """
     x,y,z >= 10 000--> x=100 y=100 --> 10 000 (but for x,y 4 or fewer digits are left)
     thus x*y < 10 000, to get x,y,z=9 digits 
     """
     def has_pandigit_prod(n):
          # factors of product=int can divide product w/o remainder
          # the largest integer i such that i*i is less than or equal to product
          for i in range(1,math.isqrt(n)+1):
               if n%i ==0:
                    tmp = str(n)+str(i)+str(n//i)
                    if "".join(sorted(tmp)) == "123456789":
                         return True
          return False
     out = sum(i for i in range(1,10000) if has_pandigit_prod(i))
     return out

if __name__ == "__main__":
     pandigital_numbers = compute()
     pandigital_numbers = set(pandigital_numbers)
     pandigital_sum = sum(pandigital_numbers)
     print (pandigital_sum)
     print (compute_v2())
