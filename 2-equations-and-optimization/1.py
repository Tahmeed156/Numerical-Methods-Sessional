import numpy as np


def unique_solution(a, n):
    """ Check is a unique solution exists """
    for i in range(n):
        if np.sum(a[i]) == 0:
            return False
    return True


def generate_ul(a, n):
    """ Generates U and L for a given A matrix """
    b = np.zeros((n, n))
    # Looping over row 0 to n
    for i in range(0, n):
        # looping over the i-th elements for all rows below i
        b[i][i] = 1
        for j in range(i+1, n):
            ratio = a[j][i] / a[i][i]
            a[j] = a[j] - a[i] * ratio
            b[j][i] = ratio
    return a.copy(), b.copy()


def get_y(L, B, n):
    """ Finding Y """
    temp = np.zeros((n, 1))
    for i in range(0, n):
        num = B[i][0]
        for j in range(0, n-1):
            num = num - temp[j][0] * L[i][j]
        temp[i][0] = num
    return temp.copy()


def get_x(U, Y, n):
    """ Finding X """
    temp = np.zeros((n, 1))
    for i in range(n-1, -1, -1):
        num = Y[i][0]
        for j in range(i+1, n):
            num = num - temp[j][0] * U[i][j]
        temp[i][0] = num / U[i][i]
    return temp.copy()


def array_output(arr, out, shape):

    for i in range(shape[0]):
        for j in range(shape[1]):
            st = str('%.4f ' % arr[i][j])
            out.write(st)
        out.write('\n')
    out.write('\n')


if __name__ == '__main__':

    A = B = []
    n = 0

    with open('in1.txt', 'r') as inp:

        # Taking input for A
        buf = []
        n = int(inp.readline())
        for i in range(0, n):
            for num in inp.readline().split():
                buf.append(float(num))
        A = np.array(buf).reshape(n, n)

        # Taking input for B
        buf = []
        for i in range(0, n):
            num = inp.readline()
            buf.append(float(num))
        B = np.array(buf).reshape(n, 1)

    U, L = generate_ul(A, n)

    Y = get_y(L, B, n)
    X = get_x(U, Y, n)

    with open('out1.txt', 'w') as out:
        array_output(L, out, (n, n))
        array_output(U, out, (n, n))
        if unique_solution(A, n):
            array_output(Y, out, (n, 1))
            array_output(X, out, (n, 1))
        else:
            out.write("No unique solution")
            exit()





