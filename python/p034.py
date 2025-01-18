# 145 -> 1! + 4! + 5! = 1 + 24 + 120 = 145
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
"""
exlude 1 and 2, N has n digits -> n*9! is the largest possible sum of the factorials of nn digits.
n=8->8*9!=2903040 -> 7 digit number, no 8 digit number  = sum of the factorials of its digits
ans = 40730
"""
import math

def compute():
    #upper_bound= 10**8 
    upper_bound = 7 * math.factorial(9)  # 2,540,160
    ans = sum(i for i in range(3,upper_bound) if i==factorial_digit_sum_v2(i))
    return ans

def factorial_digit_sum_v1(n):
    out = sum(math.factorial(int(i)) for i in str(n))
    return out

def factorial_digit_sum_v2(n):
    """    
    Precomputation: 
    -lists that store the sum of the factorials of the digits for all numbers from 0 to 9999.
    -This allows for quick lookup of the sum of the factorials of the digits for any 4-digit segment of the number.
    FACTORIAL_DIGITS_SUM_WITHOUT_LEADING_ZEROS 
    FACTORIAL_DIGITS_SUM_WITH_LEADING_ZEROS are precomputed 
    
    For very large numbers, calculating the sum of the factorials of the digits directly can be computationally expensive.
    By breaking the number into 4-digit segments and using the precomputed lists, the calculation is significantly sped up.
    
    Segmented Calculation:

    The factorial_digit_sum function processes the number in chunks of 4 digits.
    For each 4-digit segment, it looks up the precomputed sum of the factorials of the digits, adds it to the result, and then moves to the next segment.
    This reduces the number of factorial calculations needed, as each segment's result is retrieved in constant time.
    """
    out = 0
    while n>=10000:
        last4 = n%10000 # the last 4 digits of n
        out += FACTORIAL_DIGIT_SUM_WITH_LEADING_ZEROS[last4]
        n = n // 10000  # interger division to remove the last 4 digits
    out += FACTORIAL_DIGIT_SUM_WITHOUT_LEADING_ZEROS[n]
    return out
FACTORIAL_DIGIT_SUM_WITHOUT_LEADING_ZEROS   = [sum(math.factorial(int(c)) for c in str(i)) for i in range(10000)]
FACTORIAL_DIGIT_SUM_WITH_LEADING_ZEROS      = [sum(math.factorial(int(c)) for c in str(i).zfill(4)) for i in range(10000)]


if __name__ == "__main__":
    print (compute())

