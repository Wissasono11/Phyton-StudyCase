import numpy as np

def foward_elimination (A,b,n):
    for row in range(0, n-1):
        for i in range(row+1, n):
            factor = A[i, row] / A[row, row]
            for j in range(row, n):
                A[i, j] = A[i, j] - factor * A[row, j]
            
            b[i] = b[i] - factor * b[row]
        print('A = \n%s and b = %s' % (A, b))
    return A, b

def back_substitution(a,b,n):
    x= np.zeros((n,1))
    x[n-1] = b[n-1] / a[n-1, n-1]
    for row in range(n-2, -1, -1):
        sums = b[row]
        for j in range(row+1, n):
            sums = sums - a[row, j] * x[j]
        x[row] = sums / a[row, row]
    return x

def gauss(A,b):
    n = A.shape[0]

    if any(np.diag(A)==0):
        raise ZeroDivisionError(('Division by zero will occur; '
                                 'pivoting currently not supported'))
    
    A, b = foward_elimination(A,b,n)
    return back_substitution(A,b,n)

if __name__ == '__main__':
    A = np.array([[2,3,-2,-1], [2,5,-3,1], [-2,1,3,-2], [-5,2,-1,3]])
    b = np.array ([-2,7,1,8])

    print("Persamaaan A = \n", A)
    print("Hasil b = " ,b)
    x = gauss(A,b)
    print('Gauss result is x = \n %s' %x)