def gauss_jacobi(A, b, x0, max_iterations, tolerance):
    n = len(A)
    x = x0.copy()

    for iteration in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sigma) / A[i][i]

        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):
            return x_new

        x = x_new

    return x

# Contoh penggunaan
A = [[4, -1, 1],
     [4, -8, 1],
     [-2, 1, 5]]
b = [7, -21, 15]
x0 = [1, 2, 2]
max_iterations = 10000000
tolerance = 1e-1

solution = gauss_jacobi(A, b, x0, max_iterations, tolerance)
print("Solusi Gauss-Jacobi:", solution)
