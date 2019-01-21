# Note all of the starting y values are temp. input of the function is needed
# Note: the f, df, ddf because these are not right at the moment, a large diviation in the output
import math

# Settings:

endtime = 5
h = 0.0001


def realfunction(x):
    return math.exp((x**3)/3)
# This is the first ODE, dx/dt = f(t, v)
def f(x, z):
    return x*x*z
# This is the second ODE, dv/dt = f(t, x)
def df(x, z):
    return (x**3*z)/3

# Euler Method


t = 0
y = 1


while t < endtime:
    
    y = y + f(t, y)*h
    t = t + h

print("Euler value: " + str(y))

# Runge Kutta 4 all of the functions must be shifted with one d

t = 0
count = 0
y = 1

for count in range(int(endtime/h)):

    t = h*count
    count += 1


    k1 = f(t, y)
    k2 = f(t+(h/2), y+h*(k1/2))
    k3 = f(t+(h/2), y+h*(k2/2))
    k4 = f(t+h, y+h*k3)

    y += h*(k1 + 2*k2 + 2*k3 + k4)/6


print("Runge Kutta value: " + str(y))

