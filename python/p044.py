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

def np_resample(n, n_samples=100_000, random_state=21):
    """
    NumPy: draw n_samples of (j,k) with 1 <= j < k <= n.
    """
    rng = np.random.default_rng(random_state)
    # First draw j from [1..n-1], then k from [j+1..n]
    js = rng.integers(1, n,      size=n_samples)    # 1..n-1 inclusive
    # draw k from [2..n] for all, then fix those k<=j by redrawing
    ks = rng.integers(2, n+1,    size=n_samples)    # 2..n inclusive
    mask = ks <= js
    while mask.any():
        # redraw only for the “bad” entries
        ks[mask] = rng.integers(2, n+1, size=mask.sum())
        mask = ks <= js

    return list(zip(js, ks))

def py_sampling(n, n_samples=100_000, random_state=21):
    """
    Pure Python: same as above, guaranteed j < k.
    """
    rng = random.Random(random_state)
    samples = []
    for _ in range(n_samples):
        j = rng.randint(1, n-1)
        k = rng.randint(j+1, n)
        samples.append((j, k))
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


def find_best_pair_via_sampling(n,
                                 n_samples=100_000,
                                 sampler='numpy',
                                 random_state=21):
    """
    Draw n_samples random (j,k), keep only those where
      Pj+Pk  and  Pk-Pj  are both pentagonal,
    and return the pair with smallest |Pk-Pj|.
    """
    if sampler == 'numpy':
        pairs = np_resample(n, n_samples, random_state)
    else:
        pairs = py_sampling(n, n_samples, random_state)

    best_D = float('inf')
    best_pair = None

    for j, k in pairs:
        Pj = pentagon_number(j)
        Pk = pentagon_number(k)
        D  = Pk - Pj
        if D >= best_D:
            continue
        if ispentagonal(Pj + Pk) and ispentagonal(D):
            best_D = D
            best_pair = (j, k)

    return best_pair, best_D


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
    print(find_best_pair_via_sampling(3000,200_000,"numpy",21))
    t2 = time.time()
    print("Time taken: ", t2-t1)
