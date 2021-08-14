import numpy as np
import matplotlib.pyplot as plt
from enum import Enum


# Methods & Derivative function


def derivative(x, y):
    return (x + 20 * y) * np.sin(x * y)


def rk_2nd_order(x, a2, h, initial=0, group='h'):

    a1 = 1 - a2
    p1 = 0.5 / a2
    q11 = 0.5 / a2

    y = np.zeros(len(x))
    y[0] = initial

    for i in range(1, len(x)):

        k1 = derivative(x[i - 1], y[i - 1])
        k2 = derivative(x[i - 1] + p1 * h, y[i - 1] + q11 * k1 * h)

        y[i] = y[i - 1] + (a1 * k1 + a2 * k2) * h

    if group == 'h':
        plt.plot(x, y, linewidth=1, label=Method(a2).name)
    else:
        plt.plot(x, y, linewidth=1, label='h = ' + str(h))


def euler_method(x, h, initial, group='h'):

    y = np.zeros(len(x))
    y[0] = initial

    for i in range(1, len(x)):
        slope = derivative(x[i - 1], y[i - 1])
        y[i] = y[i - 1] + slope * h

    if group == 'h':
        plt.plot(x, y, linewidth=1, label="Euler_method")
    else:
        plt.plot(x, y, linewidth=1, label='h = ' + str(h))


def rk_4th_order(x, h, initial, group='h'):

    y = np.zeros(len(x))
    y[0] = initial

    for i in range(1, len(x)):

        k1 = derivative(x[i - 1], y[i - 1])
        k2 = derivative(x[i - 1] + 0.5 * h, y[i - 1] + 0.5 * h * k1)
        k3 = derivative(x[i - 1] + 0.5 * h, y[i - 1] + 0.5 * h * k2)
        k4 = derivative(x[i - 1] + h, y[i - 1] + k3 * h)

        y[i] = y[i - 1] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4) * h

    if group == 'h':
        plt.plot(x, y, linewidth=1, label="RK_4th_order")
    else:
        plt.plot(x, y, linewidth=1, label='h = ' + str(h))


class Method(Enum):
    Huen = 1 / 2
    Midpoint = 1
    Ralston = 2 / 3


# Plotting graphs by step-size (h)


plt.style.use('fivethirtyeight')

# Step sizes
h_values = [0.5, 0.1, 0.05, 0.01]
# Initial value, at x=0
ini = 4

for h in h_values:

    # Setting up Graph
    plt.figure(figsize=(12, 6))
    plt.axhline(y=0, color='lightgrey', linewidth=3)
    plt.axvline(x=0, color='lightgrey', linewidth=3)

    # Domain
    x = np.arange(0, 10.01, h)

    # Euler's Method, first order
    euler_method(x, h=h, initial=ini)

    # Huen's Method, a2=1/2
    rk_2nd_order(x, a2=1 / 2, h=h, initial=ini)

    # Midpoint Method, a2=1
    rk_2nd_order(x, a2=1, h=h, initial=ini)

    # Ralston's Method, a2=1/2
    rk_2nd_order(x, a2=2 / 3, h=h, initial=ini)

    # RK 4th Order Method
    rk_4th_order(x, h=h, initial=ini)

    plt.title("Plots for h=" + str(h))
    plt.legend()
    plt.savefig('step_size/h=' + str(h) + '.png', format='png')


# Plotting graphs according to Methods


plt.style.use('fivethirtyeight')

# Step sizes
h_values = [0.5, 0.1, 0.05, 0.01]
# Initial value, at x=0
ini = 4

# Domain
x = np.arange(0, 10.01, h)

# Euler's Method, first order

plt.figure(figsize=(12, 6))
plt.axhline(y=0, color='lightgrey', linewidth=3)
plt.axvline(x=0, color='lightgrey', linewidth=3)

for h in h_values:
    x = np.arange(0, 10.01, h)
    euler_method(x, h=h, initial=ini, group='method')

    plt.title("Euler's Method")
    plt.legend()
    plt.savefig('methods/Euler\'s Method.png', format='png')

# Huen's Method, a2=1/2

plt.figure(figsize=(12, 6))
plt.axhline(y=0, color='lightgrey', linewidth=3)
plt.axvline(x=0, color='lightgrey', linewidth=3)

for h in h_values:
    x = np.arange(0, 10.01, h)
    rk_2nd_order(x, a2=1 / 2, h=h, initial=ini, group='method')

    plt.title("Huen\'s Method")
    plt.legend()
    plt.savefig('methods/Huen\'s Method.png', format='png')

# Midpoint Method, a2=1

plt.figure(figsize=(12, 6))
plt.axhline(y=0, color='lightgrey', linewidth=3)
plt.axvline(x=0, color='lightgrey', linewidth=3)

for h in h_values:
    x = np.arange(0, 10.01, h)
    rk_2nd_order(x, a2=1, h=h, initial=ini, group='method')

    plt.title("Midpoint Method")
    plt.legend()
    plt.savefig('methods/Midpoint Method.png', format='png')


# Ralston's Method, a2=1/2

plt.figure(figsize=(12, 6))
plt.axhline(y=0, color='lightgrey', linewidth=3)
plt.axvline(x=0, color='lightgrey', linewidth=3)

for h in h_values:
    x = np.arange(0, 10.01, h)
    rk_2nd_order(x, a2=2 / 3, h=h, initial=ini, group='method')

    plt.title("Ralston's Method")
    plt.legend()
    plt.savefig('methods/Ralston\'s Method.png', format='png')

# RK 4th Order Method

plt.figure(figsize=(12, 6))
plt.axhline(y=0, color='lightgrey', linewidth=3)
plt.axvline(x=0, color='lightgrey', linewidth=3)

for h in h_values:
    x = np.arange(0, 10.01, h)
    rk_4th_order(x, h=h, initial=ini, group='method')

    plt.title("RK 4th order Method")
    plt.legend()
    plt.savefig('methods/RK 4th order Method.png', format='png')
