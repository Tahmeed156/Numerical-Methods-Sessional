import numpy as np
from matplotlib import pyplot as plt


def ln(z, n=5):
    x = z-1
    """
    Returns the values of ln(1+x),
    iterated over n times
    """
    prev = x
    sum = prev
    # Assigned first value, iterating 2 to n
    for i in range(2, n+1):
        term = prev * x * ((i-1)/i)
        if i % 2 == 0:
            sum -= term
        else:
            sum += term
        prev = term
    return sum


def ln_error(z, n=5):
    x = z-1
    """
    Returns the values of ln(1+x),
    iterated over n times
    """
    prev = x
    sum = prev
    error = []
    # Assigned first value, iterating 2 to n
    for i in range(2, n+1):
        prev_sum = sum
        term = prev * x * ((i-1)/i)
        if i % 2 == 0:
            sum -= term
        else:
            sum += term
        prev = term
        error.append(abs(sum-prev_sum)/sum)
    return error


if __name__ == '__main__':
    f1 = plt.figure()
    plt.grid(True, axis='both', color='linen', linestyle='-', linewidth=2)
    plt.axhline(y=0, color='lightgrey', linestyle='-')
    plt.axvline(x=0, color='lightgrey', linestyle='-')
    plt.ylabel('ln(1+x)')
    plt.xlabel('x')
    
    f2 = plt.figure()
    plt.grid(True, axis='both', color='linen', linestyle='-', linewidth=2)
    plt.axhline(y=0, color='lightgrey', linestyle='-')
    plt.axvline(x=0, color='lightgrey', linestyle='-')
    
    ax1 = f1.add_subplot(111)
    ax2 = f2.add_subplot(111)

    # a.
    temp = input("Enter the value of x: ")
    x = 1 + float(temp)
    temp = input("Enter the value of n: ")
    n = int(temp)
    print("The value of ln(1+x): " + str(ln(x, n)))

    # b. 
    dom = np.arange(-0.9, 1, 0.1)
    func = [np.log(i+1) for i in dom]
    ax1.plot(dom, func, color='C8', label='numpy log()')
    ax1.legend(loc='best')
    f1.savefig('1b.png', format='png', dpi=700)

    # c. 
    n_arr = [1, 3, 4, 20, 50]
    for j in range(0, 5):
        my_func = [ln(i+1, n_arr[j]) for i in dom]
        lab = str(n_arr[j]) + ' terms'
        col = 'C' + str(j)
        ax1.plot(dom, my_func, color=col, label=lab)
    ax1.legend(loc='best')
    f1.savefig('1c.png', format='png', dpi=700)

    # d. 
    plt.ylabel('Relative error')
    plt.xlabel('number of terms (2-50)')
    dom = np.arange(2, 51, 1)
    error_func = ln_error(1.5, 50)
    ax2.plot(dom, error_func, color="C2")
    f2.savefig('1d.png', format='png', dpi=700)

    plt.show()

