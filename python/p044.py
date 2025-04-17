# pentagon numbers Pn = n(3n-1)/2: 1,5,12,22,35,...
# Pi and Pk, thier sum and difference are pentagon numbers, D = |Pk-Pi| is minised

import numpy as np
import random
import time
#pentagon_number = lambda n: n*(3*n-1)//2
# //2 returns the integer division
# /2 returns the float division
def pentagon_number(n):
    return n*(3*n-1)//2
def ispentagonal(P):
    if P < 0:
        return False
    x = (1+ (1+24*P)**0.5)/6
    return x.is_integer()
# building samples
# numpy version
def np_resample(n, n_samples=10000,random_state=21):
    random_state = random_state
    rng = np.radon.defailt_rng(random_state)
    indexes = np.arange(1, n+1)
    samples = rng.choice(indexes, size=(n_samples,2),replace=True)
    return samples
def py_sampling(n, n_samples=10000, random_state=21):
    random.seed(random_state)
    samples = [
        [random.randint(1, n), random.randint(1, n)] 
        for _ in range(n_samples)
        ]
    return samples
def minimizeD(n_max):
    best_D = float('inf')
    best_pait = (None, None)
    for j in range(1,n_max):
        Pj = pentagon_number(j)
        for k in range(j+1,n_max+1):
            Pk = pentagon_number(k)
            D = Pk-Pj
            if D >= best_D:
                break
            if ispentagonal(Pk+Pj) and ispentagonal(D):     
                best_D = D
                best_pair = (j,k)
    return best_D, best_pair
import itertools


def compute():
	pentanum = PentagonalNumberHelper()
	min_d = None  # None means not found yet, positive number means found a candidate
	# For each upper pentagonal number index, going upward
	for i in itertools.count(2):
		pent_i = pentanum.term(i)
		# If the next number down is at least as big as a found difference, then conclude searching
		if min_d is not None and pent_i - pentanum.term(i - 1) >= min_d:
			break
		
		# For each lower pentagonal number index, going downward
		for j in range(i - 1, 0, -1):
			pent_j = pentanum.term(j)
			diff = pent_i - pent_j
			# If the difference is at least as big as a found difference, then stop testing lower pentagonal numbers
			if min_d is not None and diff >= min_d:
				break
			elif pentanum.is_term(pent_i + pent_j) and pentanum.is_term(diff):
				min_d = diff  # Found a smaller difference
	return str(min_d)


# Provides memoization for generating and testing pentagonal numbers.
class PentagonalNumberHelper:
	def __init__(self):
		self.term_list = [0]
		self.term_set = set()
	
	def term(self, x):
		assert x > 0
		while len(self.term_list) <= x:
			n = len(self.term_list)
			term = (n * (n * 3 - 1)) >> 1
			self.term_list.append(term)
			self.term_set.add(term)
		return self.term_list[x]
	
	def is_term(self, y):
		assert y > 0
		while self.term_list[-1] < y:
			n = len(self.term_list)
			term = (n * (n * 3 - 1)) >> 1
			self.term_list.append(term)
			self.term_set.add(term)
		return y in self.term_set

if __name__ == "__main__":
    print(pentagon_number(1020))
    print(pentagon_number(2167))
    P = pentagon_number(10)
    print(ispentagonal(P))
	
    t1 = time.time()
    print(minimizeD(4000))
    t2 = time.time()
    print (t2-t1)
	
    t1 = time.time()
    print(compute())
    t2 = time.time()
    print("Time taken: ", t2-t1)
