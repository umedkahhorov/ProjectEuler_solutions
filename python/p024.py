import itertools

def find_nth_permutation(iterable,n):
    count = 0
    for perm in itertools.permutations(iterable):
        count+=1
        if count==n:
            return perm

def compute():
    elements = list(range(10))
    out = itertools.islice(itertools.permutations(elements),999999,None)
    return "".join(str(x) for x in next(out))
    
if __name__ == "__main__":
    a = list(range(10))
    print(find_nth_permutation(a,1000000))
    print (compute())