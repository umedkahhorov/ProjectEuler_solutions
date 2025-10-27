from math import isqrt
# Перестановка Permuted Multiples
def compare_permutations(a, b):
    str_a, str_b = str(a), str(b)
    return len(str_a) == len(str_b) and sorted(str_a) == sorted(str_b)

num_multiples = lambda x,n : [ x*i for i in range(1,n+1)]

def compute():
    x = 1
    while True:
        numbers = num_multiples(x,6)
        res = [compare_permutations(numbers[0],numbers[i]) for i in range(1,len(numbers))]
        if all(res):
            return x
        x += 1


if __name__ == "__main__":
    res = num_multiples(142857,6)
    print(res)
    print(compute())
