"""
585(10 ​=1001001001(2)​.
Read 585 from left to right or right to left—it’s the same sequence of digits, 
so it’s a decimal palindrome
"""
def is_palindromic_base(n):
    """
    Check if a number is a palindrome in base 10 and 2.
    """
    s_decimal = str(n)
    s_binary = bin(n)[2:]
    return s_decimal == s_decimal[::-1] and s_binary == s_binary[::-1]

def compute():
    m = 10**6
    ans = sum(i for i in range(m) if is_palindromic_base(i))
    return ans

if __name__ == "__main__":
    print (is_palindromic_base(585))
    print (compute())