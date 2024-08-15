"""
<p>Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
\begin{align}
1634 &amp;= 1^4 + 6^4 + 3^4 + 4^4\\
8208 &amp;= 8^4 + 2^4 + 0^4 + 8^4\\
9474 &amp;= 9^4 + 4^4 + 7^4 + 4^4
\end{align}
</p><p class="smaller">As $1 = 1^4$ is not a sum it is not included.</p>
<p>The sum of these numbers is $1634 + 8208 + 9474 = 19316$.</p>
<p>Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.</p>
"""

# Set the upper bound for the fifth power sum, start with the fifth power of 9 - the largest single-digit number
max_fifth_power = 9**5
# Initialize the upper bound with the maximum fifth power
upper_bound = max_fifth_power
# Initialize the number of digits to 1
num_digits = 1
# Loop until the upper bound has more digits than the current number of digits
while upper_bound >= 10**num_digits:
    # Increment the number of digits
    num_digits += 1
    # Add the maximum fifth power to the upper bound to increase its value
    upper_bound += max_fifth_power
def compute_sum_of_digits(upper_bound):
    out=0
    for j in range(2,upper_bound):
        a = str(j)
        a = [int(i) for i in a]
        sum_of_digits = sum([i**5 for i in a])
        if j == sum_of_digits:
           out += sum_of_digits
           print(j,out)
    return None
compute_sum_of_digits(upper_bound)
