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

# Find abundant numbers up to a certain limit (e.g., 28123)
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
print (abundant_sums)
# Find the sum of all positive integers that cannot be written as the sum of two abundant numbers
result = sum(i for i in range(limit + 1) if i not in abundant_sums)

print("The sum of all positive integers that cannot be written as the sum of two abundant numbers is:", result)
