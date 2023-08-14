import numpy as np
import math

def if_prime(n: int)-> bool:
    if n<=1:
        return False
    elif n<=3:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3,math.floor(math.sqrt(n))+1,2):
            if n%i ==0:
                return False
        return True
    
def isPrime(n):
    if n==1:
        return False
    if n<4:
        return True
    if n%2==0:
        return False
    if n<9:
        return True
    if n%3==0:
        return False
    else:
        r = math.floor(math.sqrt(n))
        f=5
        while f<=r:
            if n%f ==0:
                return False
            if n%(f+2)==0:
                return False
            f = f + 6
        return True



    