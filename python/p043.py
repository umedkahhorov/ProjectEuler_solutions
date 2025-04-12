# generate all 0 to 9 pandigital numbers
# sub-string divisibility property:d2d3d4:2,d3d4d5:3,d4d5d6:5,d5d6d7:7,d6d7d8:11,d7d8d9:13,d8d9d10:17
# out = 16695334890
from itertools import permutations

def generate_all_0_to_9_pandigital():
    digits = "0123456789"
    pandigitals = (int("".join(i)) for i in permutations(digits))
    return list(pandigitals)

def ispandigital(n):
    # simply check if the digits of n are exactly "1" to len(n)
    s = str(n)
    if set(s)==set("0123456789"[:len(s)]):
        return n
    else:
        return 0
    
def generate_all_0_to_9_pandigital_v2():
    digits = "0123456789"
    numbers = []
    for i in permutations(digits):
        num = int("".join(i))
        if ispandigital(num):
            numbers.append(num)
    return numbers

divisib_prop = lambda nlist,dlist: all(int(nlist[i:i+3]) % d == 0 for i,d in zip(range(1,8),dlist))

def compute():
    all_pandigitals = generate_all_0_to_9_pandigital()
    dlist = [2,3,5,7,11,13,17]
    result = 0
    for pandigital in all_pandigitals:
        if divisib_prop(str(pandigital), dlist):
            result += pandigital
    return result

if __name__ == "__main__":
    #n = 9876325041
    #print(ispandigital(n))
    #n = 9851260347
    #print(ispandigital(n))
    #print(generate_all_0_to_9_pandigital())
    #print(generate_all_0_to_9_pandigital_v2())
    print(compute())