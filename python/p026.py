def recurring_cycle(n):
    remainder = 1
    seen = {}
    cycle = ""
    index = 0

    while remainder !=0 and remainder not in seen:
        seen[remainder] = index
        remainder *=10
        digit = remainder // n
        cycle +=str(digit)
        remainder %=n
        index += 1
    if remainder !=0:
        start_of_cycle = seen[remainder]
        recurring_cycle = seen[remainder]
        recurring_cycle = cycle[start_of_cycle:]
        return str(recurring_cycle)
    else:
        return str(0)
    
def compute():
    limit=1000
    out = [0] * (limit-1)
    for i in range(1,limit):
        out[i-1] = recurring_cycle(i)
    max_recur = max(out,key=len)
    max_recur = len(max_recur)
    return max_recur

import itertools
def compute_v2():
    ans = max(range(1,1000), key=recipocal_cycle_len)
    return ans

def recipocal_cycle_len(n):
    seen = {}
    x = 1
    for i in itertools.count():
        if x in seen:
            return i - seen[x]
        else:
            seen[x] = i
            x = x*10%n


if __name__ == "__main__":
    print(recurring_cycle(984))
    print (compute())
    print (compute_v2())

