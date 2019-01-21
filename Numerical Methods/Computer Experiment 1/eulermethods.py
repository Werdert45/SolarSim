import math

def f(x):
    return math.log(5)**x



# Euler Method

t = 0
h = 0.01

y = f(0)

while t < 10:
    n = t
    n1 = t + h
    slope = (f(n1)-f(n))/(n1-n)
    y = y + slope*h

    t += h

erroreuler = abs(f(10)-y)
magnitudeerroreuler = erroreuler/y
print(magnitudeerroreuler)

# Backward Euler method

t = 0

dt = 0.01

y = math.log(5)

while t < 10:
    n = t

    n1 = t+dt

    n2 = t+2*dt

    slope = (f(n2)-f(n1))/(n2-n1)

    y = y + slope*dt

    t += dt

errorbackeuler = abs(f(10)-y)
magnitudeerrorbackeuler = errorbackeuler/y
print(magnitudeerrorbackeuler)
