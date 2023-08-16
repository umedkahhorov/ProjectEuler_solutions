
import time
import numpy as np 


with open('data/data11.txt', 'r') as file:
    grid_list = [list(map(int, row.split())) for row in file]
input_array = np.array(grid_list)
# sol 1
def extract_4x4(input_array, start_row, start_col):
    results = []
    for y in range(start_row, len(input_array)):
        for x in range(start_col, len(input_array[y])):
            if x + 4 <= len(input_array[y]):
                results.append(grid_product(input_array, x, y, 1, 0))
            if y + 4 <= len(input_array):
                results.append(grid_product(input_array, x, y, 0, 1))
            if x + 4 <= len(input_array[y]) and y + 4 <= len(input_array):
                results.append(grid_product(input_array, x, y, 1, 1))
            if x - 3 >= 0 and y + 4 <= len(input_array):
                results.append(grid_product(input_array, x, y, -1, 1))
    return results
def grid_product(input_array, ox, oy, dx, dy):
    result = 1
    for i in range(4):
        result *= input_array[oy + i * dy][ox + i * dx]
    return result
CONSECUTIVE = 4
out = extract_4x4(input_array,0,0)
print (max(out))
# sol 2
def calculate_products_4x4(input_array):
    rows, cols = input_array.shape
    products = []
    
    for c in range(cols - 3):
        for r in range(rows - 3):
            submatrix = input_array[r:r+4, c:c+4]
            row_products = np.prod(submatrix, axis=1)
            col_products = np.prod(submatrix, axis=0)
            diag_products = [np.prod(np.diagonal(submatrix)), np.prod(np.diagonal(np.flip(submatrix, axis=1)))]
            products.extend(row_products)
            products.extend(col_products)
            products.extend(diag_products)
    return max(products)
out = calculate_products_4x4(input_array)
print (out)
# sol 3
def product_of_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
def calculate_products_4x4(input_array):
    rows, cols = input_array.shape
    products = []
    max_product = float('-inf')
    
    for c in range(cols - 3):
        for r in range(rows - 3):
            submatrix = input_array[r:r+4, c:c+4]
            
            row_products = [product_of_list(row) for row in submatrix]
            col_products = [product_of_list(submatrix[:, col]) for col in range(4)]
            diag_products = [product_of_list([submatrix[i, i] for i in range(4)]),
                             product_of_list([submatrix[i, 3 - i] for i in range(4)])]
            
            products.extend(row_products)
            products.extend(col_products)
            products.extend(diag_products)
            
            product = max(max(row_products), max(col_products), max(diag_products))
            max_product = max(max_product, product)
            
    return max_product
out = calculate_products_4x4(input_array)
print (out)
