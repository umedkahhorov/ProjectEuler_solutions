# latural number - postive int starting from 1 (or 0) - 0,1,2,3,4,5,6,7,8,9,10,...
# natural numbers - non negative integers, whole numbers
def compute():
    ans = max(sum(int(c) for c in str(a**b))
              for a in range(100)
              for b in range(100)
              )
    return str(ans)
print(compute()) # 972
