import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from enum import Enum

# Collecting data

x = []
y = []
intervals = []

with open('F:/BUET/2-1/Code/CSE 218 Numerical Methods/Offline 4 - Numerical Integration/IO/input-1.txt') as file:

    n = int(file.readline())

    coordinates = file.readlines()

    for c in coordinates:
        coor = c.split()

        if x != []:
            intervals.append(round(float(coor[0]) - xc, 6))

        xc = float(coor[0])
        yc = float(coor[1])

        x.append(xc)
        y.append(yc)

cnt = 1
con_int = []

for i in range(1, n - 1):

    if intervals[i] == intervals[i - 1]:
        cnt += 1
        continue
    else:
        con_int.append(cnt)
        cnt = 1
con_int.append(cnt)

print(con_int)


# Methods for Integration


def trapezoid(a, x, y):
    return (x[a + 1] - x[a]) * (y[a] + y[a + 1]) * 0.5


def simpson_13(a, b, x, y):
    h = (x[b] - x[a]) / 2
    return (h / 3) * (y[a] + 4 * y[a + 1] + y[a + 2])


def simpson_38(a, b, x, y):
    h = (x[b] - x[a]) / 3
    return ((3 * h) / 8) * (y[a] + 3 * y[a + 1] + 3 * y[a + 2] + y[a + 3])


class Integration(Enum):
    Trapezoid = 1
    Simpson_13 = 2
    Simpson_38 = 3


# Determining Intervals


methods = []

for interval in con_int:

    if interval == 1:
        methods.append(Integration.Trapezoid)

    else:

        m = interval % 3

        if m == 0:

            for i in range(int(interval / 3)):
                methods.extend([Integration.Simpson_38] * 3)

        elif m == 1:

            for i in range(int((interval - 4) / 3)):
                methods.extend([Integration.Simpson_38] * 3)

            for i in range(2):
                methods.extend([Integration.Simpson_13] * 2)

        elif m == 2:

            for i in range(int((interval - 2) / 3)):
                methods.extend([Integration.Simpson_38] * 3)

            for i in range(1):
                methods.extend([Integration.Simpson_13] * 2)

print(f'Trapezoidal rule: {methods.count(Integration.Trapezoid)} intervals')
print(f'1/3 rule: {methods.count(Integration.Simpson_13)} intervals')
print(f'3/8 rule: {methods.count(Integration.Simpson_38)} intervals')


# Finding Integral and Plotting


area = 0
a = 0
index = 0

plt.style.use('fivethirtyeight')
plt.figure(figsize=(10, 6))

plt.axhline(y=0, color='lightgrey', linewidth=3, linestyle='-')
plt.axvline(x=0, color='lightgrey', linewidth=3, linestyle='-')

plt.plot(x, y, marker='d', markersize=6, linewidth=0)

while True:

    if index >= len(methods):
        break

    if methods[index] == Integration.Trapezoid:
        area += trapezoid(index, x, y)
        plt.fill_between(x[index:index + 2], y[index:index + 2], color='blue', alpha=0.2,
                         interpolate=True, label="Average developer wins")
        index += 1
    elif methods[index] == Integration.Simpson_13:
        area += simpson_13(index, index + 2, x, y)
        plt.fill_between(x[index:index + 3], y[index:index + 3], color='blue', alpha=0.5,
                         interpolate=True, label="Average developer wins")
        index += 2
    elif methods[index] == Integration.Simpson_38:
        area += simpson_38(index, index + 3, x, y)
        plt.fill_between(x[index:index + 4], y[index:index + 4], color='blue', alpha=0.8,
                         interpolate=True, label="Average developer wins")
        index += 3

custom = [
    Line2D([0], [0], color='blue', lw=4, alpha=0.2),
    Line2D([0], [0], color='blue', lw=4, alpha=0.4),
    Line2D([0], [0], color='blue', lw=4, alpha=0.8),
]
plt.legend(custom, ["Trapezoid", "Simpson 1/3",
                    "Simpson 3/8"], loc="upper left", )
plt.title('Numerical Integration')
plt.show()

print(f'Value of Integral: {area}')
