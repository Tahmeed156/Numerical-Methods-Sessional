import numpy as np
np.set_printoptions(precision=2, suppress=True)


def print_array(arr, h, shape):
    for i in range(len(h)):
        print('%8s' % h[i], end='\t\t')
    print("")
    for i in range(shape[0]):
        for j in range(shape[1]):
            print('%8.2f' % arr[i][j], end='\t\t')
        print("")
    print("")


if __name__ == '__main__':

    buff = []
    n = m = siz = 0

    with open('in2.txt', 'r') as inp:
        for val in inp.readline().split():
            buff.append(float(val) * (-1.0))

        buff.append(0.0)
        # n is the number of co-efficients
        n = len(buff)

        lines = inp.readlines()
        for l in lines:
            for i in l.split():
                buff.append(float(i))

        # m is the number of rows (constraints + 1)
        m = int(len(buff)/n)
        # total columns
        siz = n+m

    A = np.zeros((m, siz))

    head = []
    for i in range(n-1):
        head.append('x' + str(i+1))
    head.append('F')
    head.append('Z')
    for i in range(n+1, n+m):
        head.append('s' + str(i-n))

    # Iterating from 0 to m rows (all rows)
    for i in range(m):
        # Iterating over 0 to n cols (coeff cols)
        for j in range(n):
            # Saving coefficients from the previous array
            A[i][j] = buff[i*n+j]
        A[i][n+i] = 1

    # Derived the matrix to start the calculation
    print_array(A, head, A.shape)

    while np.min(A[0][A[0]<n-1]) < 0:
        col = np.argmin(A[0])
        ratios = [np.inf]
        for i in range(1, m):
            ratios.append(A[i][n-1] / A[i][col])

        row = np.argmin(ratios)
        A[row] /= A[row][col]
        for i in range(m):
            if i == row:
                continue
            A[i] -= A[i][col]*A[row]
        print_array(A, head, A.shape)

    print("Maximum value = %0.2f" % A[0][n-1])
    for i in range(n-1):
        l = list(A[:, i])
        ans = 0.0
        if l.count(1) == 1 and l.count(0) == m-1:
            ans = A[l.index(1)][n-1]
        print("x" + str(i+1) + ": " + str(ans))
