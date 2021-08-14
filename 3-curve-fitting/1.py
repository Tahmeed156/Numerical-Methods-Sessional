from matplotlib import pyplot as plt
import numpy as np


def coefficients(x_arr, y_arr, order):

    left = np.empty((order+1, order+1))
    right = np.empty((order+1, 1))

    for i in range(order+1):
        for j in range(order+1):
            left[i][j] = np.power(x_arr, i+j).sum()
        right[i][0] = np.power(x_arr, i).dot(y_arr).sum()

    return np.linalg.solve(left, right)


def regression(x_arr, y_arr, coeffs):

    st = np.power(y_arr - np.mean(y_arr), 2).sum()

    diff = 0
    pow = 0
    for c in coeffs:
        diff += c * np.power(x_arr, pow)
        pow += 1

    y_arr = y_arr.reshape((1, len(y_arr)))
    sr = np.power(y_arr - diff, 2).sum()
    r = np.power((st - sr)/st, 0.5)

    return r


if __name__ == '__main__':

    with open('data.txt', 'r') as inp:

        x = []
        y = []
        n = 0

        while True:
            coordinate = inp.readline().split()
            if not coordinate:
                break
            x.append(float(coordinate[0]))
            y.append(float(coordinate[1]))
            # print(x[n], y[n])
            n += 1

        print("Number of input values: " + str(n))

        x = np.array(x)
        y = np.array(y).reshape(len(y), 1)

        # SETTING UP GRAPH

        plt.figure(figsize=(12, 8))
        plt.grid(True, axis='both', color='linen', linestyle='-', linewidth=2)
        plt.axhline(y=0, color='lightgrey', linestyle='-')
        plt.axvline(x=0, color='lightgrey', linestyle='-')

        plt.scatter(x, y, color='C0', s=2)

        print("\n================= ORDER = 1 =================\n")

        coeffs = coefficients(x, y, 1)
        for i in range(2):
            print('a' + str(i) + ' = ' + str(coeffs[i][0]))
        print("Regression coefficient \n\t" + str(regression(x, y, coeffs)))

        # Graph

        dom = np.linspace(min(x), max(x), 1000)
        func = 0
        pow = 0
        for c in coeffs:
            func += c * np.power(dom, pow)
            pow += 1

        plt.plot(dom, func, color='C1', label="Order 1")

        print("\n================= ORDER = 2 =================\n")

        coeffs = coefficients(x, y, 2)
        for i in range(3):
            print('a' + str(i) + ' = ' + str(coeffs[i][0]))
        print("Regression coefficient \n\t" + str(regression(x, y, coeffs)))

        # Graph

        dom = np.linspace(min(x), max(x), 1000)
        func = 0
        pow = 0
        for c in coeffs:
            func += c * np.power(dom, pow)
            pow += 1

        plt.plot(dom, func, color='C2', label="Order 2")

        print("\n================= ORDER = 3 =================\n")

        coeffs = coefficients(x, y, 3)
        for i in range(4):
            print('a' + str(i) + ' = ' + str(coeffs[i][0]))
        print("Regression coefficient \n\t" + str(regression(x, y, coeffs)))

        # Graph

        dom = np.linspace(min(x), max(x), 1000)
        func = 0
        pow = 0
        for c in coeffs:
            func += c * np.power(dom, pow)
            pow += 1

        plt.plot(dom, func, color='C3', label="Order 3")

        # Graph setup

        plt.title("Curve fitting offline")
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.legend(loc='best')

        plt.show()
