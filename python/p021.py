# sum of amicable Numbers. For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110; therefore d(220)=284 . 
# The proper divisors of 284 are 1, 2, 4, 71, 142; so d(284)=220 .
#################### Sol 1 ####################
import math
def get_divisors(n):
    div_sum = 1  # Start with 1 as all numbers have 1 as a proper divisor
    sqrt_num  = int(math.sqrt(n))
    for i in range(2,sqrt_num+1):
        if n % i == 0:
            div_sum+=i
            if i != n//i: # Ensure not to add the same divisor twice for perfect squares
                div_sum+=n//i  
    return div_sum
def amicable_sum(limit):
    out = 0
    for i in range(2,limit):
        div_sum_a = get_divisors(i)
        div_sum_b = get_divisors(div_sum_a)
        if i != div_sum_a and i == div_sum_b:
            out += i
    return out
#################### Sol 2 ####################
# We first compute a table of sum-of-proper-divisors, then we use it to test which numbers are amicable.
def compute():
    divisorsum = [0]*10000
    for i in range(1,len(divisorsum)):
        for j in range(i*2,len(divisorsum),i):
            divisorsum[j] +=i
    
    ans = 0
    for i in range(1,len(divisorsum)):
        j = divisorsum[i]
        if j != i and j < len(divisorsum) and divisorsum[j] ==i:
            ans +=i
    return ans
#################### Sol 3 ####################
def SumOfProperDivisors(n):
    sum = 1
    for f in range(2,n):
        if n % f ==0:
            sum +=f
    return sum
def SumOfProperDivisors_v2(n):
    if n == 1:
        return 0
    else:
        r = math.floor(math.sqrt(n))
    #//first take into account the case that n is a perfect square.
    if r*r == n:
        sum = 1 + r
        r = r - 1
    else:
        sum = 1
    if n % 2 !=0:
        f = 3
        step = 2
    else:
        f = 2
        step = 1
    while f<=r:
        if n % f == 0:
            sum = sum + f + (n//f)
        f = f + step
    return sum
def compute_v2():
    sum = 0
    for a in range(2,10000):
        b = SumOfProperDivisors_v2(a)
        if b>a:
            if SumOfProperDivisors_v2(b)==a:
                sum += a+b
    return sum

if __name__ == "__main__":
    # Calculate the sum of all amicable numbers under 10,000
    limit = 10000
    #result = amicable_sum(limit)
    #print(f"The sum of all amicable numbers under {limit} is: {result}")
    #print (compute())
    #print (compute_v2())
    #print (get_divisors(220))
    print (SumOfProperDivisors_v2(220))