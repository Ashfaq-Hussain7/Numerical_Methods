#Program 1:
#Finding roots of non linear equations using bisection method.


def bisect(func, a, b, E):

    while (True) :

      c=(a+b)/2

      if b-c <= E:
        return c

      elif solve_fn(func,c) <= 0:
        a=c

      else :
        b=c

def solve_fn(eq:list, x:int):
  value = 0
  for i in range (0,len(eq),2) :
    value += eq[i]*(x**eq[i+1])
  return value

eq=[1,6,-1,1,-1,0]
E=0.00005
l=1
u=2
print("THE ROOT OF THE EQUATION IS: " , bisect(eq, l, u, E))