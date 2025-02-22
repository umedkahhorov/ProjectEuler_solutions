# perimeter of right angled triangle
# summ of all its sides (a+b+c) = p,  a = height, b = base, and c = hypotenuse.
# a^2 + b^2 = c^2
# b^2 = c^2 - a^2
# a^2 = c^2 - b^2
# a + b = p^2 + 2ab / 2p
# b = p^2 - 2ap / 2p - 2a
# b go up to (p-a)//2+1 -> b<=c or c >= b, a<=b<=c

import math
import time

def compute():
    Perimeter = 1000
    num_solutions = {}
    for p in range(5, Perimeter+1):
        upper_bound = math.floor(p/2)
        max_solutions = 0
        for a in range(1, upper_bound):
            b = (p**2 - 2*p*a) / (2*p - 2*a)
            if b.is_integer():
                max_solutions += 1
        num_solutions[p] = max_solutions
    max_p = max(num_solutions, key=num_solutions.get)
    return max_p, num_solutions[max_p]

def count_solutions(p):
    result = 0
    for a in range(1,p+1):
        for b in range(a,(p-a)//2+1):
            c = p-a-b
            if a*a + b*b == c*c:
                result += 1
    return result

def compute_v2():
    ans = max(range(1,1001), key=count_solutions)   
    return ans


if __name__ == "__main__":
    t1 = time.time()
    print(compute())
    t2 = time.time()
    print('time:', t2-t1)
    t1 = time.time()
    print(compute_v2())
    t2 = time.time()
    print('time:', t2-t1)

