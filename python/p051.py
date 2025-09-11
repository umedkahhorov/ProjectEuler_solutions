# prime digit replacement
# searching for the tiniest prime that, when some of its digits are swapped out with the same digit, produces 8 different prime numbers. - “eight prime value family”
from math import isqrt
from eulerlib import get_prime_list
from eulerlib import is_prime_list

def compute():
    plist = get_prime_list(100)
    plist = [i for i in plist if i>=10 and str(i)[-1]=="3"]
    print(plist)

if __name__ == "__main__":
    plist = get_prime_list(100)
    compute()
    print(plist)
