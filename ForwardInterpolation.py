#Program 8:
#Estimate value using Newtons Forward Interpolation Method.

import numpy as np

def newtons_forward_interpolation(x, y, target):
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
    result = y[0]

    # Compute interpolation
    u = (target - x[0]) / h
    for i in range(1, n):
        term = 1
        for j in range(i):
            term *= (u - j)
            term /= (j + 1)
        result += term * divided_diff[0, i]

    return result

# Example usage:
x = [3, 5, 7, 9]
y = [180, 150, 120, 90]
target = 4

estimated_value = newtons_forward_interpolation(x, y, target)
print(f"The estimated value at x = {target} is: {estimated_value}")