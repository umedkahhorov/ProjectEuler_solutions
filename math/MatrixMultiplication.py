"""
For AA (size m x n) and BB (size n x p), the resulting matrix ABAB (size m x p) is computed as:
(AB)_{ij} = sum(a_{ik} * b_{kj} for k in range(n))
This is the dot product of the ii-th row of AA with the jj-th column of BB, applied systematically for all rows and columns.
"""

def matrix_multiplication(A, B):
    # get the dimen of A, B
    m,n = len(A),len(A[0])
    n2,p = len(B), len(B[0])
    if n!=n2:
        print("Matrix multiplication is not possible")
    AB = [[0 for _ in range(p)] for _ in range(m)] 

    for i in range(m): # iterate over rows of A
        for j in range(p): # iterate over columns of B
            # compute the dot product of row i of A and column j of B
            for k in range(n):
                AB[i][j] +=A[i][k] * B[k][j]

    return AB

if __name__ == "__main__":
    A = [
        [1,2,3],
        [4,5,6],
    ]
    B = [
        [7,8],
        [9,10],
        [11,12],
    ]
    AB = matrix_multiplication(A,B)
    print(AB)
