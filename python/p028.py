import numpy as np
# Starting with the number and moving to the right in a clockwise direction a by spiral is formed as:
a = np.array([[21,22,23,24,25],[20,7,8,9,10],[19,6,1,2,11],[18,5,4,3,12],[17,16,15,14,13]])
#  the sum of the numbers on the diagonals is 101
# What is the sum of the numbers on the diagonals in a by spiral formed in the same way
print (a.diagonal(axis1=0,axis2=1),np.fliplr(a).diagonal())
print (np.sum(a.diagonal())+np.sum(np.fliplr(a).diagonal())-1)
# correct answer is 669171001.0
# define a center with value 1
def create_array(a=5):
    out = np.zeros((a,a))
    col_idx = a//2
    row_idx = a//2
    out[row_idx,col_idx]=1
    return out
def corners_spiral_array(n):
    corner_value_max = n*n
    corner_value_min = corner_value_max-(n*4-5)
    #print (corner_value_max,corner_value_min)
    corner_values = np.flip(np.arange(corner_value_min,corner_value_max+1,1))
    arr = np.zeros((n,n))
    arr[0,:]     = corner_values[:n][::-1]
    arr[1:,0]    = corner_values[n:2*n-1]
    arr[-1,1:]   = corner_values[2*n-1:3*n-2]
    arr[1:-1,-1] = corner_values[3*n-2:][::-1] 
    return arr
def diagonals(size):
    arr = corners_spiral_array(size)
    left_diagonal = np.fliplr(arr).diagonal()
    left_diagonal = left_diagonal[left_diagonal!=0].sum()
    right_diagonal = arr.diagonal()
    right_diagonal = right_diagonal[right_diagonal!=0].sum()
    return left_diagonal+right_diagonal
def compute():
    n=6
    out=0
    for i in range(3,1002,2):
        out+=diagonals(i)
    return out
print (compute()+1)
# solution 2 
# the top right corner n^2
# the top left corner n^2 - (n - 1)
# the bottom left  n^2 - 2(n - 1)
# the bottom right is n^2 - 3(n - 1)
# final  4n^2 - 6(n - 1)
def compute():
    n=1001
    ans=1
    ans+= sum(4*i*i-6*(i-1) for i in range(3,n+1,2))
    return ans
compute()
# solution 3
def compute_diagonal_sum(n):
    total_sum = 1  # Starting with the center value
    current_value = 1
    
    for layer in range(1, (n // 2) + 1):
        side_length = 2 * layer
        for corner in range(4):
            current_value += side_length
            total_sum += current_value
            
    return total_sum

# Example usage
n = 1001
result = compute_diagonal_sum(n)
print(f"The sum of the numbers on the diagonals in a {n}x{n} spiral is {result}.")
