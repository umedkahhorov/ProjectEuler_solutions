# multiples of 3 and 5

def multiples_sum(a,b,limit):
    """
    find the sum all the multiples of a and b below limit
    """
    sum_ab = [i for i in range(1,limit) if i%3==0 or i%5 == 0]

    return sum(sum_ab)

if __name__ == "__main__":
    print ('Project Euler 1')
    print (multiples_sum(3,5,1000))