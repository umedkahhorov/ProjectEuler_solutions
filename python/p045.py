# triangle number Tn = n(n+1)/2 - 1 3 6 10 15
## that can be represented in the form of a triangular grid of points where the first row contains a single element and each subsequent row contains one more element than the previous one.

# pentagonal number Pn = n(3n-1)/2 - 1 5 12 22 35
## Every pentagonal number is 1/3 of a triangular number. Every pentagonal number is exactly one-third of some triangular number.
## In fact, the nth pentagonal number shows up as one-third of the (3n−1)th triangular number.

# hexagonal number Hn = n(2n-1) - 1 6 15 28 45
## A polygonal number and 6-polygonal number. The first few are 1, 6, 15, 28, 45, ... Every hexagonal number is a triangular number 
## Each nnth hexagonal number equals the (2n−1)th triangular number.


### T_285= P_165= H_143= 40755

# answer
# Indexes (tri, pent, hex): 55385 31977 27693
# Value = 1533776805 1533776805 1533776805

### m
### n_pent = (m+1)/3 if (m + 1) % 3 == 0 
### n_hexa = (m+1)/2 m must be odd for n to be an integer. If m is even, Tm is not a hexagonal number.

import math

triangle_number = lambda m: m*(m+1)//2
pentagonal_number = lambda m: m*(3*m-1)//2
hexagonal_number = lambda m: m*(2*m-1)

def compute():
    i = 285 # is odd and a multiple of 3"
    while True:
        i +=1
        if i % 2 == 1:
            n_tria = i
            Tn = triangle_number(i)
            # is Tₘ pentagonal, test if T is pentagonal by inverting P_n = n(3n−1)/2:
            # Pn = n(3n-1)/2 = T
            D = 1 + 24*Tn
            sqrtD = int(math.isqrt(D))
            if D == sqrtD*sqrtD: # Perfect‐square discriminant
                if (1 + sqrtD) % 6 == 0: # # (1 + sqrt(D)) must be divisible by 6
                    n_pent = (1 + sqrtD)//6
                    n_hexa = (i+1)//2
                    Pn = pentagonal_number(n_pent)
                    Hn = hexagonal_number(n_hexa)
                    if pentagonal_number(n_pent) == hexagonal_number(n_hexa) == Tn:
                        print("Indexes (tri, pent, hex):", n_tria, n_pent, n_hexa)
                        print("Value =", Tn,Pn,Hn)
                        break
if __name__ == "__main__":
    compute()

