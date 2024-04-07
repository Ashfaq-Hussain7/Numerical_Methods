#Program 11
#Simpson's 1/3 rd Rule

import math

def f(x):
    return math.exp(-x)

def simpsons_one_third(f, a, b, n):

    if n % 2 != 0:
        raise ValueError("Number of intervals must be even for Simpson's 1/3 rule.")

    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(x_i) for x_i in x]

    integral = y[0] + y[-1]  # Include the first and last terms

    # Add terms with coefficient 4
    for i in range(1, n, 2):
        integral += 4 * y[i]

    # Add terms with coefficient 2
    for i in range(2, n - 1, 2):
        integral += 2 * y[i]

    integral *= h / 3
    return integral

# Main function
def main():

    a = float(input("Enter the lower limit of integration: "))
    b = float(input("Enter the upper limit of integration: "))


    n = int(input("Enter the number of intervals (must be even): "))

    # Calculate the approximation of the definite integral
    integral = simpsons_one_third(f, a, b, n)
    print("Approximation of the definite integral of e^(-x) using Simpson's 1/3 rule:", integral)

if __name__ == "__main__":
    main()

