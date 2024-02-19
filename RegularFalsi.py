#Program 2:
#Finding roots of non linear equations using false position method.
def regula_falsi(func, a, b, E):

    while True:
        c = (a * solve_fn(func, b) - b * solve_fn(func, a)) / (solve_fn(func, b) - solve_fn(func, a))

        if abs(solve_fn(func, c)) <= E:
            return c

        elif solve_fn(func, c) * solve_fn(func, a) < 0:
            b = c

        else:
            a = c


def solve_fn(eq:list, x:int):
  value = 0
  for i in range (0,len(eq),2) :
    value += eq[i]*(x**eq[i+1])
  return value

eq = [1, 3, -4, 1, -9, 0]
E = 0.00005
l = 2
u = 3

print("THE ROOT OF THE EQUATION IS:", regula_falsi(eq, l, u, E))