import time 

def countRoutes(m,n):
    if n==0 or m==0:
        return 1
    return countRoutes(m,n-1) + countRoutes(m-1,n)
t1 = time.time()
out = countRoutes(2,2)
t2 = time.time()
print ('1',out,t2-t1)

cache = {}
def countRoutes(m,n):
    if n == 0 or m == 0:
        return 1
    if (m,n) in cache:
        return cache[(m,n)]
    cache[(m,n)] = countRoutes(m,n-1) + countRoutes(m-1,n)
    return cache[(m,n)]
t1 = time.time()
out = countRoutes(20,20)
t2 = time.time()
print ('2',out,t2-t1)

def countRoutes(m,n):
    # # Create a 2D array of size (m + 1) x (n + 1)
    grid = [[0]*(n+1) for _ in range(m+1)]
    #print (grid)
    for i in range(m+1):
        grid[i][0] = 1
    #print (grid)
    for j in range(n+1):
        grid[0][j] = 1
    #print (grid)
    for i in range(1,m+1):
        for j in range(1,n+1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    #print (grid)
    return grid[m][n]
t1 = time.time()
out = countRoutes(4,4)
t2 = time.time()
print (3,out,t2-t1)

def countRoutes(n):
    result = 1
    for i in range(1,n+1):
        result = result * (n+i)//i
    return result
t1 = time.time()
out = countRoutes(20)
t2 = time.time()
print (3,out,t2-t1)



