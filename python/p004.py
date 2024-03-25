import numpy as np
import sys
"""Find the largest palindrome made from the product of two 3-digit numbers."""
def palindromic_number_v1():
    ans = max(i*j
            for i in range(100,1000)
            for j in range(100,1000)
            if str(i*j) == str(i*j)[::-1])
    return ans

def palindromic_number_v2():
    nmax = 0
    for i in range(999,100,-1):    # dow from 999 to 100
        if i*i < nmax:             # check loop is less the sqrt of highest number  
            break
        for j in range(i,100,-1):  # further narrow search space
            n = i*j
            if check_palindromic(n):
                if n > nmax:
                    nmax = n
                break
    return nmax

def check_palindromic(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    print ('Project Euler 4')
    print (palindromic_number())
    n = palindromic_number()
    print (check_palindromic(n))
    print (palindromic_number_v2())
