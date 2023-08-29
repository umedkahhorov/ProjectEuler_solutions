import eulerlib, functools, sys
import time


# We compute the Collatz chain length for every integer in the range according to the iteration rule.
# Also, we cache the Collatz value for all integer arguments to speed up the computation.
"""
def compute():
	sys.setrecursionlimit(3000)
	ans = max(range(1, 1000000), key=collatz_chain_length)
	return str(ans)
@functools.cache
def collatz_chain_length(x):
	if x == 1:
		return 1
	if x % 2 == 0:
		y = x // 2
	else:
		y = x * 3 + 1
	return collatz_chain_length(y) + 1
if __name__ == "__main__":
	start = time.time()
	print(compute())
	end = time.time()
	print (end-start)
"""
# sol 1 
def compute(n: int)-> int:
    if n==1:
        return 1
    if n % 2 == 0:
        return 1 + compute(n/2)
    else:
        return 1 + compute(int(3*n)+1)
#print (compute(20))
#longest_chain: int = 0
#answer: int = -1
#start = time.time()
#for n in range(13, int(1e6)-1):
#    if compute(n) > longest_chain:
#        longest_chain = compute(n)
#        answer = n
#end = time.time()
#print (answer,end-start)
# 23 sec


