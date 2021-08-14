import numpy as np
from matplotlib import pyplot as plt


def secant_method(func, guess_1, guess_2, error, max_iter):
    """Secant method | Recursion method"""
    # Finding Xr+1 using Xr(guess_2) and Xr-1(guess_1)
    new_guess = guess_2 - ((guess_1 - guess_2)/(func(guess_1) - func(guess_2)))*func(guess_2)

    if abs((new_guess-guess_2)/new_guess*100) < error or max_iter <= 1:
        return new_guess, 500-max_iter+1
    else:
        return secant_method(func, guess_2, new_guess, error, max_iter-1)


def false_position_method(func, lower_bound, upper_bound, error, max_iter):
    """False position method | Do while method"""
    if func(lower_bound)*func(upper_bound) > 0:
        print("Result is not bracketed by bounds")
        return 0, 0

    approx, steps = 100, 0
    prev_guess, new_guess = 0, 0
    while approx >= error and steps < max_iter:
        prev_guess = new_guess
        new_guess = upper_bound \
                    - ((lower_bound - upper_bound) / (func(lower_bound) - func(upper_bound))) \
                    * func(upper_bound)

        if func(new_guess) * func(upper_bound) < 0:
            # y value for x=new_guess exists below x-axis
            lower_bound = new_guess
        elif func(new_guess) * func(lower_bound) < 0:
            # y value for x=new_guess exists above x-axis, OR is 0
            upper_bound = new_guess

        if steps < 1:
            steps = 1
            continue
        else:
            approx = (abs((prev_guess - new_guess) / new_guess) * 100)
            steps += 1

    return new_guess, steps


def given_func(x):
    """The defined function/curve"""
    # return x ** 3 - 2400 * x ** 2 - 3 * x + 2
    if x < -2:
        print("Error: Root of a negative number for x=" + str(x))
    try:
        a = (x / (1 - x)) * np.sqrt(6 / (2 + x)) - 0.05
        return a
    except ZeroDivisionError:
        print("Error: Dividing by zero for x=" + str(x))
        return 0


if __name__ == '__main__':
    
    ''' Answer (a) '''
    x = np.arange(0, 0.035, 0.001)
    y = (x/(1-x)) * np.sqrt(6/(2+x)) - 0.05
    
    # Setting up graph
    plt.plot(x, y)
    plt.grid(True, axis='both', color='linen', linestyle='-', linewidth=2)
    plt.axhline(y=0, color='lightgrey', linestyle='-')
    plt.axvline(x=0, color='lightgrey', linestyle='-')
    plt.show()
    
    ''' Answer (b) '''
    answer, steps = false_position_method(given_func, -1.9, 0.9, 0.01, 500)
    print("False position method: value=" + str(answer) + ", steps=" + str(steps))
    answer, steps = secant_method(given_func, -1.9, 0.9, 0.01, 500)
    print("Secant method: value=" + str(answer) + ", steps=" + str(steps))
