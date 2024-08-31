"""
the currency is made up of pound, $, and pence, p, and there are eight coins in
general circulation:
1p, 2p, 5p, 10p, 20p, 50p, $1 (100p) and $2 (200p).
It is possible to make $2 in the following way:
1 $1 + 1 50p + 2 20p + 1 5p + 1 2p + 3 1p
How many different ways can $2 be made using any number of coins?
"""
coins = [1, 2, 5, 10, 20, 50,100,200]
def count_coins(coins,m,target_sum):
    if target_sum==0:
        return 1
    if target_sum <=0:
        return 0
    if m<=0 and target_sum >= 1:
        return 0
    
    return count_coins(coins,m-1,target_sum)+count_coins(coins,m,target_sum-coins[m-1])

target_sum = 200
number_of_ways = count_coins(coins,len(coins),target_sum)
print (number_of_ways) # 73682
##
amount = 200
coins = [1, 2, 5, 10, 20, 50,100,200]
def count_v1(target,m,coins):
    if m<=1:
        return 1
    res = 0
    while target>=0:
        res = res + count_v1(target,m-1,coins)
        target = target - coins[m-1]
    return res
print (count_v1(amount,8,coins))
##
coins = [1, 2, 5, 10, 20, 50,100,200]
target = 200
coin_min,coin_max = 2,8
memo = [[0 for _ in range(coin_max+1)] for _ in range(target+1)]
print (len(memo))
def count_v2(target,m,coins):
    if m<=1:
        return 1
    t = target
    if memo[t][m]>0:
        return memo[t][m]
    res = 0
    while target>=0:
        res = res + count_v2(target,m-1,coins)
        target = target - coins[m-1]
    memo[t][m] = res
    return res
print (count_v2(target,8,coins))
##
coins = [1, 2, 5, 10, 20, 50,100,200]
target = 200
ways = [0 for _ in range(target+1)]
ways[0] = 1
for i in range(1,8+1):
    for j in range(coins[i-1],target+1):
        ways[j]=ways[j] + ways[j-coins[i-1]]
print (ways[target])
