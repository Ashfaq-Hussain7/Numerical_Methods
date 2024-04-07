#Program 10
#Estimate value using Lagrange's Interpolation Method.

# To represent a data point corresponding to x and y = f(x)
class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def interpolate(f: list, xi: float, n: int) -> float:
    # Initialize result
    result = 0.0
    for i in range(n):
        # Compute individual terms of above formula
        term = f[i].y
        for j in range(n):
            if j != i:
                term = term * (xi - f[j].x) / (f[i].x - f[j].x)
        # Add current term to result
        result += term
    return result

# Driver Code
if __name__ == "__main__":
    # Number of data points
    n = int(input("Enter the number of data points: "))

    # Create an array of known data points
    f = []
    print("Enter the data points:")
    for i in range(n):
        x = float(input(f"Enter x[{i}]: "))
        y = float(input(f"Enter y[{i}]: "))
        f.append(Data(x, y))

    # Obtain the data point corresponding to x = xi
    xi = float(input("Enter the value of x for interpolation: "))
    print("Value of f(x) is:", interpolate(f, xi, n))