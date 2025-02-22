# Pandigital Multiples
# 192x1 = 192
# 192x2 = 384
# 192x3 = 576
# 192384576 is a 1 through 9 pandigital
# Find the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1
# ans = 932718654
import math
import time

def compute():
    upper_bound = 10**9-1
    largest_pandigital = 0
    for i in range(1,math.isqrt(upper_bound)+1):
        n = 1
        pandigital_multiples = []
        while True:
            pandigital_multiples.append(str(i*n))
            cat_str = "".join(pandigital_multiples)
            if len(cat_str) == 9:
                if "".join(sorted(cat_str)) == "123456789":
                    val = int(cat_str)
                    if val > largest_pandigital:
                        largest_pandigital = val

            if len(cat_str) >= 9:
                break
            n += 1
    return largest_pandigital


def panProduct(num,arr):
    product = ""
    for i in arr:
        product += str(i*num)
    return int(product)

arr = [1]
best = 0
testProduct = 0
for i in range(2,10):
    arr.append(i)
    testNum = 1
    while testProduct<1000000000:
        testProduct = panProduct(testNum,arr)
        if testProduct>best and testProduct<1000000000 and "".join(sorted(str(testProduct)))=="123456789":
            best = testProduct
        testNum += 1

print(best)

from itertools import count, imap 
def ispandigital( seed):
   digits = str( seed)
   for i in count(2):
      ndig = len( digits)
      if ndig < 9: digits += str( seed * i)
      elif ndig == 9 and set( digits) == set( '123456789'):
         return int( digits)
      else: return False

    print (max( imap( ispandigital, xrange( 1, 10000))))


if __name__ == "__main__":
    t1 = time.time()
    print(compute())
    t2 = time.time()
    print('time:', t2-t1)