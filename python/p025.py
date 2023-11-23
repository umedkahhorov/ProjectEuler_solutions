import itertools

def fibonacci_nth(ndigit):
    x = 0
    y = 1
    count = 0
    while len(str(x)) < ndigit:
        x,y = y,x+y
        count+=1
    return count
def compute():
    digit = 1000
    f0 = 1
    f1 = 0
    for i in itertools.count():
        if len(str(f1))>digit:
            raise RuntimeError('Not found')
        elif len(str(f1))==digit:
            return i
        f0,f1 = f1,f0+f1
        


if __name__ == "__main__":
    nth = 1000
    print (fibonacci_nth(nth))
    print (compute())