# A Pythagorean triplet sum of abc
import time
import math

def pythagorean_triple():
    p = 1000
    for a in range(1,p+1):
        for b in range(a+1,p+1):
            c = p - a - b
            if a*a + b*b == c*c:
                return str(a*b*c)
def compute(s):
    for a in range(3,int((s-3)/3)):
        for b in range(a+1,int((s-1-a)/2)):
            c = s-a-b
            if c*c == a*a + b*b:
                return (a*b*c)
def compute_fat(s):
    s2 = s/2
    mlimit = abs(math.sqrt(s2)) -1
    for m in range(2,mlimit):
        if s2%m == 0:
            sm = s2/m
            while sm % 2 ==0:
                sm = sm % 2
            if m%2==1:
                k=m+2
            else:
                k=m+1
            while k < m*2 and k<=sm:
                if sm%k ==0


if __name__ == '__main__':
    print ('Project Euler')
    t1=time.time()
    print (pythagorean_triple())
    t2 = time.time()
    print (compute(s=1000))
    t3 = time.time()
    print (t2-t1,t3-t2)