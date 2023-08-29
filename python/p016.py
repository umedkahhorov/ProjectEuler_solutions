import time 
"""
2**15 = 32768 3+2+7+6+8=26
2**1000?
answer 1366
"""
def compute(p):
    ans = 2**p
    #out = 0
    #for i in str(ans):
    #    out += int(i)
    out = sum(int(i) for i in str(ans)) 
    return out

if __name__ == "__main__":
    t1 = time.time()
    out = compute(1000)
    t2 = time.time()
    print(out,t2-t2)
 