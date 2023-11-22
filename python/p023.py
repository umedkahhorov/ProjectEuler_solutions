# 4179871
import math
def sum_divisors(n):
    # Function to calculate the sum of divisors of a number
    div_sum = 1
    sqrt_num = int(n ** 0.5)
    #sqrt_num = math.sqrt(n)
    for i in range(2, sqrt_num + 1):
        if n % i == 0:
            div_sum += i
            if i != n // i:
                div_sum += n // i
    return div_sum
def compute():
    limit = 28123
    divisorsum = [0]*limit
    for i in range(1,limit):
        for j in range(i*2,limit,i):
            divisorsum[j] +=i
    abundantnums = [i for (i,x) in enumerate(divisorsum) if x>i]
    expressible = [False]*limit
    for i in abundantnums:
        for j in abundantnums:
            if i+j < limit:
                expressible[i+j] = True
            else:
                break
    ans = sum(i for (i,x) in enumerate(expressible) if not x)
    return ans
if "__main__" == __name__:
    # Find abundant numbers up to a certain limit (e.g., 28123)
    print (compute())
    limit = 28123
    abundant_numbers = []
    for i in range(12, limit + 1):
        if sum_divisors(i) > i:
            abundant_numbers.append(i)
    # Create a set of all numbers that can be represented as the sum of two abundant numbers
    abundant_sums = set()
    for i in abundant_numbers:
        for j in abundant_numbers:
            if i + j <= limit:
                abundant_sums.add(i + j)
    # Find the sum of all positive integers that cannot be written as the sum of two abundant numbers
    result = sum(i for i in range(limit + 1) if i not in abundant_sums)
    print("The sum of all positive integers that cannot be written as the sum of two abundant numbers is:", result)
