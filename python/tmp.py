import numpy as np

# Define the input array and the filter
input_array = np.array([[8, 2, 22, 97],
                        [49, 49, 99, 40],
                        [81, 49, 31, 73],
                        [52, 70, 95, 23]])

filter_array = np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])

# Perform element-wise multiplication (convolution)
result_array = input_array * filter_array
#result = np.prod(result_array)

print("Input Array:")
print(input_array)
print("\nFilter Array:")
print(filter_array)
print("\nConvolution Result:")
print(result_array)

# Define the input array and the filter
input_array = [[8, 2, 22, 97],
               [49, 49, 99, 40],
               [81, 49, 31, 73],
               [52, 70, 95, 23]]

filter_array = [[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]]

# Get the diagonal elements of the input array and compute their product
diagonal_elements = [input_array[i][i] for i in range(len(input_array))]
result = 1
print (diagonal_elements)
for element in diagonal_elements:
    result *= element

print("Input Array:")
for row in input_array:
    print(row)
print("\nFilter Array:")
for row in filter_array:
    print(row)
print("\nProduct of Diagonal Elements:")
print(result)

