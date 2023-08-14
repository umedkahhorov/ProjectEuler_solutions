import time
import numpy as np 


with open('data/data11.txt', 'r') as file:
    #for i in file:
    #    print (i.split()[0])
    #print (file.readline())
    grid_list = [list(map(int, row.split())) for row in file]
grid_array = np.array(grid_list)
#print(grid_array)
#print (grid_array.shape)
#from scipy.signal import convolve2d
# Define the filter
filter_array = np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])

# Perform the 2D convolution
#output_array = convolve2d(grid_array, filter_array, mode='valid')
import numpy as np

def convolve2d(input_array, filter_array):
    input_shape = input_array.shape
    filter_shape = filter_array.shape

    # Compute output shape
    output_shape = (input_shape[0] - filter_shape[0] + 1, input_shape[1] - filter_shape[1] + 1)

    # Initialize output array
    output_array = np.zeros(output_shape)

    # Perform convolution
    for i in range(output_shape[0]):
        for j in range(output_shape[1]):
            output_array[i, j] = np.prod(input_array[i:i+filter_shape[0], j:j+filter_shape[1]] * filter_array)

    return output_array

# Define the input array and the filter
input_array = np.array([[8, 2, 22, 97],
                        [49, 49, 99, 40],
                        [81, 49, 31, 73],
                        [52, 70, 95, 23]])

filter_array = np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])

# Perform convolution
result_array = convolve2d(input_array, filter_array)

print("Input Array:")
print(input_array)
print("\nFilter Array:")
print(filter_array)
print("\nConvolution Result:")
print(result_array)
