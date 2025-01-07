"""
49/98 = 4/8 non trivail
30/50 = 3/5 trivail
two digits in the numerator and denominator
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

ans:
numer = [16, 19, 26, 49] 
denom = [64, 95, 65, 98]
8/800 = 100
"""
from math import gcd
import math
from functools import reduce
def compute():
    """
    we iterate of lists (10,100)
    drop:
      if fraction>=1
      if n,d % 10 !=0
      if n,d consist of same digists
    keep non common digits
    appen to the output list
    """
    numerators = list(range(10, 100))
    denominators = list(range(10, 100))
    nl, dl = [], []

    for n in numerators:
        for d in denominators:
            if n < d and n % 10 != 0 and d % 10 != 0:
                n_digits = set(str(n))
                d_digits = set(str(d))
                common_digits = n_digits & d_digits

                if len(common_digits) == 1:
                    non_common_n = n_digits - common_digits
                    non_common_d = d_digits - common_digits

                    if len(non_common_n) == 1 and len(non_common_d) == 1:
                        d1 = int(non_common_n.pop())
                        d2 = int(non_common_d.pop())

                        if n / d == d1 / d2:
                            nl.append(n)
                            dl.append(d)
    print(nl, dl)
    return None

def compute2():
	# Consider an arbitrary fraction n/d:
	#   Let n = 10 * n1 + n0 be the numerator.
	#   Let d = 10 * d1 + d0 be the denominator.
	# As stated in the problem, we need 10 <= n < d < 100.
	# We must disregard trivial simplifications where n0 = d0 = 0.
	# 
	# Now, a simplification with n0 = d0 is impossible because:
	#   n1 / d1 = n / d = (10*n1 + n0) / (10*d1 + n0).
	#   n1 * (10*d1 + n0) = d1 * (10*n1 + n0).
	#   10*n1*d1 + n1*n0 = 10*d1*n1 + d1*n0.
	#   n1*n0 = d1*n0.
	#   n1 = d1.
	#   This implies n = d, which contradicts the fact that n < d.
	# Similarly, we cannot have a simplification with n1 = d1 for the same reason.
	# 
	# Therefore we only need to consider the cases where n0 = d1 or n1 = d0.
	# In the first case, check that n1/d0 = n/d;
	# in the second case, check that n0/d1 = n/d.
	numer = 1
	denom = 1
	for d in range(10, 100):
		for n in range(10, d):
			n0 = n % 10
			n1 = n // 10
			d0 = d % 10
			d1 = d // 10
			if (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == n * d0):
				numer *= n
				denom *= d
	return str(denom // math.gcd(numer, denom))




if __name__ == "__main__":
    compute()
    print(compute2())