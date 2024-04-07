#Program 12
#Simpson's 3/8 th Rule

import math

def f(x):
    return 1/(1+(x**2))

def simpsons_three_eighth(f, a, b, n):

    if n % 3 != 0:
        raise ValueError("Number of intervals must be a multiple of 3 for Simpson's 3/8 rule.")

    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(x_i) for x_i in x]

    integral = y[0] + y[-1]  # Include the first and last terms

    # Add terms with coefficient 3
    for i in range(1, n, 3):
        integral += 3 * y[i]

    # Add terms with coefficient 3
    for i in range(2, n, 3):
        integral += 3 * y[i]

    # Add terms with coefficient 2
    for i in range(3, n - 1, 3):
        integral += 2 * y[i]

    integral *= 3 * h / 8
    return integral

# Main function
def main():
    a = float(input("Enter the lower limit of integration: "))
    b = float(input("Enter the upper limit of integration: "))

    n = int(input("Enter the number of intervals (must be a multiple of 3): "))

    # Calculate the approximation of the definite integral
    integral = simpsons_three_eighth(f, a, b, n)
    print("Approximation of the definite integral of e^(-x) using Simpson's 3/8 rule:", integral)

if __name__ == "__main__":
    main()