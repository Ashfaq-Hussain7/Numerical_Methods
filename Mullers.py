#Program 4:
#Finding roots of non linear equations using Muller's method.

import cmath

def mullers_method(func, x0, x1, x2, epsilon=0.0005, max_iterates=100):
    x = [x0, x1, x2]
    iterations =  0

    while iterations < max_iterates:
        h0 = x[1] - x[0]
        h1 = x[2] - x[1]

        d1 = (func(x[1]) - func(x[0])) / h0
        d2 = (func(x[2]) - func(x[1])) / h1

        a = (d2 - d1) / h0 + h1
        b = a * h1 + d1
        c = func(x[2])

        # Check if the discriminant is close to zero
        discriminant = b**2 -  4*a*c
        if abs(discriminant) <  1e-10:
            print("Discriminant is close to zero.")
            return None, iterations+1

        D = cmath.sqrt(discriminant)

        if abs(b + D) > abs(b - D):
            value = b + D
        else:
            value = b - D

        x3 = x[2] - ((2*c) / value)

        Ea = ((x3 - x[2]) / x3) *  100

        if abs(Ea) < epsilon:
            return x3, iterations+1

        x[0] = x[1]
        x[1] = x[2]
        x[2] = x3
        iterations +=  1

# Quadratic equation
def quad_eqtn(x):
    return x**3 -  13*x -  12

# Initial guesses
x0 =  4.5
x1 =  5.5
x2 =  5

root, iterations = mullers_method(quad_eqtn, x0, x1, x2)

if root is not None:
    print(f"Root: {root}")
    print(f"Iterations: {iterations}")
else:
    print("Method did not converge.")