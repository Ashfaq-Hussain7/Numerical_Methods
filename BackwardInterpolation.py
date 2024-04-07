#Program 9
##Estimate value using Newtons Bacward Interpolation Method.

import numpy as np

def newtons_backward_interpolation(x, y, target):

    n = len(x)
    h = x[1] - x[0]

    # Create a table to store divided differences
    divided_diff = np.zeros((n, n))
    divided_diff[:, 0] = y

    # Calculate divided differences
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i, j] = divided_diff[i+1, j-1] - divided_diff[i, j-1]

    # Initialize result
    result = y[-1]

    # Compute interpolation
    u = (target - x[-1]) / h
    for i in range(1, n):
        term = 1
        for j in range(i):
            term *= (u + j)
            term /= (j + 1)
        result += term * divided_diff[n-i-1, i]

    return result

# Example usage with user input:
n = int(input("Enter the number of data points: "))
x = []
y = []

# Reading input data points
print("Enter the data points:")
for i in range(n):
    x_val = float(input(f"x[{i}]: "))
    y_val = float(input(f"y[{i}]: "))
    x.append(x_val)
    y.append(y_val)

target = float(input("Enter the target x-coordinate for interpolation: "))

# Perform interpolation
estimated_value = newtons_backward_interpolation(x, y, target)
print(f"The estimated value at x = {target} is: {estimated_value}")