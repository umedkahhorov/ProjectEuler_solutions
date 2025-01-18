
def factorial(n):
    """
    Compute the factorial of n using dynamic programming.
    """
    # Initialize a list to store intermediate factorial values
    dp = [1] * (n + 1)

    # Compute the factorial iteratively
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * i
    
    # Return the factorial of n
    return dp[n]

if __name__ == "__main__":
    # Print the factorial of 10
    print(factorial(10))
    
    # Compute the factorial of 100 and convert it to a string
    ans = str(factorial(100))
    
    # Initialize a variable to store the sum of digits
    out = 0
    
    # Iterate over each digit in the string
    for n in ans:
        # Add the integer value of each digit to out
        out += int(n)
    # out = sum(int(digit) for digit in ans)
    # Print the sum of the digits of the factorial of 100
    print(out)