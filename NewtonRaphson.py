#Program 3:
#Finding roots of non linear equations using Newton Raphson method.


import sympy as sp

def calculate_derivative(equation, variable='x'):
    x = sp.symbols(variable)
    expression = sp.sympify(equation)
    derivative = sp.diff(expression, x)
    return derivative

def newton_raphson(func, derivative_func, x0, tol=1e-6, max_iter=100):
    x = x0
    iterations = 0

    while abs(func(x)) > tol and iterations < max_iter:
        x = x - func(x) / derivative_func(x)
        iterations += 1

    return x, iterations

equation = input("Enter the equation in terms of 'x': ")

# Define the function and its derivative
x = sp.symbols('x')
user_function = sp.sympify(equation)
user_derivative = sp.diff(user_function, x)

# Convert to numerical functions
func = sp.lambdify(x, user_function, 'numpy')
derivative_func = sp.lambdify(x, user_derivative, 'numpy')

a=float(input("Enter the lower bound of the interval (a): "))
b=float(input("Enter the upper bound of the interval (b): "))

initial_guess = float(input("Enter the initial guess for the root: "))

# Apply the Newton-Raphson method
root, iterations = newton_raphson(func, derivative_func, initial_guess)

print(f"The root of the equation is: {root}")
print(f"Iterations: {iterations}")

