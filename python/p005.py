import numpy as np
import pandas as pd
import math
def prime_factorization(n):
    prime_factors = []
    c = 2 # smallest prime number
    while n > 1:
        if n % c == 0:
            n = n / c
            prime_factors.append(c)
        else:
            c = c + 1
    n,m = np.unique(prime_factors,return_counts=True)
    return n,m
def lcm(nlist,primes_val=True):
    primes = []
    powers = []
    for i in range(len(nlist)): 
        n,m = prime_factorization(nlist[i])
        if len(n)>1:
            for j in range(len(n)):
                primes.append(n[j])
                powers.append(m[j])
        else:
            primes.append(n[0])
            powers.append(m[0])
    df = pd.DataFrame(columns=['primes','powers'])
    df.loc[:,'primes'] = primes
    df.loc[:,'powers'] = powers
    primes_df = df.iloc[df.groupby(['primes']).apply(lambda x: x['powers'].idxmax())] 
    primes_df.loc[:,'mult'] = primes_df['primes'].values ** primes_df['powers'].values
    primes_df = primes_df.reset_index(drop=False)
    ans = primes_df['mult'].cumprod()
    if primes_val:
        return primes_df['primes'].values
    else:
        return ans.iloc[-1]

def compute(k,p):
    N,i = 1,0
    check = True
    lim = math.sqrt(k)
    a = np.zeros_like(p)
    while p[i] < k:
        #print (p[i-1])
        a[i] = 1
        if check:
            if p[i] <= lim:
                a[i] = math.floor(math.log(k) / math.log(p[i]))
            else:
                check = False
        N = N * p[i]**a[i]
        i = i+1
        if i==len(p):
            break
    return N 


if __name__ == "__main__":
    print ('Project Euler 5')
    nlist = list(range(2,21))
    n = lcm(nlist)
    print (n) 
    print (compute(20,[2,3,5,7,11,13,17,19]))

    