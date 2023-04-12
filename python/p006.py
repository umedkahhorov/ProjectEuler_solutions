import numpy as np
import math

def squares_of_sum_v1(n):
    ans = n*(n+1)/2
    ans = ans**2
    return ans 

def sum_of_squares_v1(n):
    numer = n*(n+1)*(2*n+1)
    ans = numer / 6
    return ans



if __name__ == "__main__":
    print ("Project Euler 6")
    print (sum_of_squares_v1(100))
    print (squares_of_sum_v1(100))
    print (squares_of_sum_v1(100)-sum_of_squares_v1(100))
