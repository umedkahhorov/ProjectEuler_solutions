import itertools
import time
from math import floor
"""
The following iterative sequence is defined 
for the set of positive integers
n->n/2(n is even), n-> 3n+1(n is odd)

Using the rule above and starting with , 
we generate the following sequence:
13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1 ) 
contains 10 terms. Although it has not been proved yet (Collatz Problem),
 it is thought that all starting numbers finish at 1 .
Which starting number, under one million, produces the longest chain?
answer 837799-->525
"""
def sequence(n: int) -> int:
    n_terms = 1
    while n > 1:
        if n & 1 == 0:
            n //= 2
            n_terms += 1
        else:
            n = 3 * n + 1
            n_terms += 1
    return n_terms

def compute():
    max_n_terms = 0
    max_n_terms_starting_num = 0
    for n in range(13, int(1e6)):
        n_terms = sequence(n)
        if n_terms > max_n_terms:
            max_n_terms = n_terms
            max_n_terms_starting_num = n
    return max_n_terms_starting_num
# sol 2
# Memoization involves storing the computed sequence lengths 
# for previously visited numbers so that 
# we don't need to recalculate them. 
def compute_f():
    max_n_terms = 0
    max_n_terms_starting_num = 0
    computed_lengths = {}
    for n in range(12,int(1e6)):
        current_num = n
        n_terms = 1
        while current_num!=1:
            if current_num in computed_lengths:
                n_terms += computed_lengths[current_num]
                break
            if current_num & 1 == 0:
                current_num//=2
            else:
                current_num = 3 * current_num + 1
            n_terms +=1
        computed_lengths[n]=n_terms
        if n_terms>max_n_terms:
            max_n_terms=n_terms
            max_n_terms_starting_num=n
    return max_n_terms_starting_num
start = time.time()
out = compute()
end = time.time()
print(out,end-start)
print (sequence(out))
start = time.time()
out = compute_f()
end = time.time()
print(out,end-start)
print (sequence(out))
    