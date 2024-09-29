from math import exp
from matplotlib import pyplot as plt
import numpy as np

def euler(x_dot, h, T, x_0):
    t = 0
    time_steps = [0]
    x = x_0
    x_values = [x_0]
    while t < T:
        x = x + h * x_dot(x, t)
        x_values.append(x)
        t = t + h
        time_steps.append(t)
    return time_steps, x_values

def heun(x_dot, h, T, x_0):
    t = 0
    time_steps = [0]
    x = x_0
    x_values = [x_0]
    while t < T:
        x_euler = x + h * x_dot(x, t)
        x = x + h * (x_dot(x, t) + x_dot(x_euler, t + h)) / 2
        x_values.append(x)
        t = t + h
        time_steps.append(t)
    return time_steps, x_values

def exact(x, T):
    time_steps = np.arange(0.0, T, 0.01)
    x_values = [x(t) for t in time_steps]
    return time_steps, x_values

a = 0.5
x = lambda t: exp(a * t)
x_dot = lambda x, t: a * x

# c = 0
# x = lambda t: t * t + c
# x_dot = lambda x, t: 2 * t

# c = 2
# x_dot = lambda x, t: t * t + 1
# x = lambda t: (t * t * t) / 3 + t + c

h = 0.5
T = 20
    
exact_time_steps, exact_x_values = exact(x, T)
euler_time_steps, euler_x_values = euler(x_dot, h, T, x(0))
heun_time_steps, heun_x_values = heun(x_dot, h, T, x(0))
plt.plot(exact_time_steps, exact_x_values, label='exact')
plt.plot(euler_time_steps, euler_x_values, label='euler')
plt.plot(heun_time_steps, heun_x_values, label='heun')
# plt.plot(heun_steps, heun, label='heun')

plt.legend()
plt.show()