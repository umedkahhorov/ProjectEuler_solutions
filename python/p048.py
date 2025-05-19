# 1**1 + 2**2 + 3**3 ... 10**10 = 10405071317 --> last ten digits to 1000**1000
# This sequence grows extremely fast—much faster than exponential sequences 2**n
# the Sondow constant n**n --> 1/n**n
# sum(n**n for n in range(1,11)) - to calculate each term individually
# last digit (1**1 mod 10) + (2**2 mod 10) .. (10**10 mod 10) 

# approach 1
m = 1001
last_10_digits = 10000000000 # 1e10
total = sum(n**n for n in range(1,m+1))
print(total % last_ 10_digits)

# approach 2 - modulo
#for n in range(1,m+1):
#  total += pow(n,n,1e10)
total = sum(pow(n,n,1e10) for n in range(1,m+1))
print(total % last_ 10_digits)

