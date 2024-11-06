import numpy as np

def gauss_jordan(a,b):
    a = np.array(a, float)
    b = np.array(b, float)

    n = len(b)
    ab = np.column_stack((a,b))

    for k in range(n):
        if ab[k,k] == 0:
         for i in range(k+1, n):
            if ab[i,k] != 0:
                ab[k,i] = ab[[i,k]]
                break

            pivot = ab[k,k]
            ab[k] /= pivot

            for i in range(n):
                if i != k:
                 factor = ab[i,k]
            ab[i] -= factor * ab[[i,k]]

            x = ab[:, -1]
            a = ab[:, :-1]
            return x,a
        a = [[3,5]],[[2,3]]
        b = [[9,5]]

        solution, transformed_a = gauss_jordan(a,b)
        print("Hasil nilai matirks diagonal: ")
        print(transformed_a)
        print(solution)