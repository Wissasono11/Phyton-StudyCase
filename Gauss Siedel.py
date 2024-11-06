print("Nama\t: Bayu Wicaksono\nNIM\t: 23106050002\nProdi\t: Informatika")
def seidel(a, x ,b):        
    n = len(a)                    
    for j in range(0, n):         
        # temp variable d to store b[j] 
        d = b[j]                   

        # to calculate respective xi, yi, zi 
        for i in range(0, n):      
            if(j != i): 
                d-=a[j][i] * x[i] 
        # updating the value of our solution         
        x[j] = d / a[j][j]

    # returning our updated solution            
    return x
n = 3                              

x = [1, 2, 2]                         
a = [[4, 1, 7],[4, -8, 1],[-2, 1, 5]] 
b = [7,-21,15]

print("Persamaan A = ",a)
print("Hasil B = ",b)
print("x = ",x)

for i in range(0, 25):             
    x = seidel(a, x, b) 
    #print each time the updated solution 
    print("Current x = ",x) 
print("x1, x2, x3 = ",x)