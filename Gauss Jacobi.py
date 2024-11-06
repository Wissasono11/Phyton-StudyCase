import numpy as np

ITERATION_LIMIT=1000
A = np.array([[4.,-1.,1.] , [4.,-8.,1.] , [-2.,1.,5.]])
B = np.array([7.,-21.,15.])

print("Persamaan : ")
for i in range(A.shape[0]):
	row = ["{}*x{}".format(A[i,j] , j+1)
		for j in range(A.shape[1])]
	print(" + ".join(row),"=",B[i])

x = np.zeros_like(B)
for it_count in range(ITERATION_LIMIT):
	print("Solusi sekarang :",x)
	x_new = np.zeros_like(x)

	for i in range(A.shape[0]):
		s1 = np.dot(A[i , :i] , x[:i])
		s2 = np.dot(A[i , i + 1:] , x[i+1:])
		x_new[i] = (B[i]-s1-s2)/A[i,i]
	if np.allclose(x,x_new,atol=1e-10,rtol=0.):
		break
	x = x_new
print("Solution: ")
print("x1,x2,x3,x4" , x)
