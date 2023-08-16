import time
import math
from eulerlib import sqrt
import itertools
"""
The sequence of triangle numbers is generated by adding the natural numbers. So the th triangle number would be 1+2+3+4+5+6+7=28,  
factors of the first seven triangle numbers: 28: 1,2,4,7,14,28 --> 5
What is the value of the first triangle number to have over five hundred divisors?
correct_answer = 76576500
"""
"""
# brute force
#t = 1 # trinagle number 
#a = 1
#count = 0
#while count<500:
#    count = 0
#    a = a + 1
#    t = t + a
#    for i in range(1,t+1):
#        if t % i == 0:
#            count +=1
#print (t)
t = 1
a = 1
count = 0
start = time.time()
while count<=500:
    count = 0 
    a = a + 1
    t = t + 1
    ttx = int(sqrt(t))
    for i in range(1,ttx+1):
        if t % i == 0:
            count = count + 2
    if t == ttx * ttx:
        count -=1
end = time.time()
print (t,end-start)
"""

def compute():
    ith_triangle = 0
    for i in itertools.count(1):
        ## This is the ith triangle number, i.e. num = 1 + 2 + ... + i = i * (i + 1) / 2
        ith_triangle +=i  
        if num_divisors(ith_triangle)>500:
              return str(ith_triangle)
# Returns the number of integers in the range [1, n] that divide n.
def num_divisors(n):
    end = sqrt(n)
    result = sum(2
            for i in range(1,end-1)
            if n % i == 0)
    if end**2 == n:
         result -=1 
    return result

if __name__ == "__main__":
     start = time.time()
     ans = compute()
     end = time.time()
     print (ans,end-start)


        

