print("Nama : Bayu Wicaksono")
print("NIM  : 23106050002")
print("Prodi: Informatika")
print("========================================")

def f(x):
    return x**2 - 8*x+10

error = 0.0001
a = 1
b = 2.4

def bisection(a,b):
    iteration = True
    i = 0
    max_iter = 50
    while iteration and i < max_iter:
        if f(a)*f(b) < 0:
            x = (a+b)/2
            if f(a)*f(x) < 0:
                b = x
                print("jika f(a)*f(x) < 0 maka b = x, b= ", x)
            if f(b)*f(x) < 0:
                a = x
                print("jika f(b)*f(x) < 0 maka a = x, b= ", x)
            if abs(a-b) < error:
                iteration = False
            else:
                i+=1
        else:
            print('tidak ditemukan akar')
    
    print('x=', x)

bisection(a,b)


"""Nama : Bayu Wicaksono
NIM  : 23106050002
Prodi: Informatika
========================================
jika f(a)*f(x) < 0 maka b = x, b=  1.7
jika f(b)*f(x) < 0 maka a = x, b=  1.35
jika f(b)*f(x) < 0 maka a = x, b=  1.525
jika f(a)*f(x) < 0 maka b = x, b=  1.6124999999999998
jika f(a)*f(x) < 0 maka b = x, b=  1.5687499999999999
jika f(b)*f(x) < 0 maka a = x, b=  1.546875
jika f(a)*f(x) < 0 maka b = x, b=  1.5578124999999998
jika f(a)*f(x) < 0 maka b = x, b=  1.55234375
jika f(b)*f(x) < 0 maka a = x, b=  1.549609375
jika f(a)*f(x) < 0 maka b = x, b=  1.5509765624999998
jika f(b)*f(x) < 0 maka a = x, b=  1.55029296875
jika f(a)*f(x) < 0 maka b = x, b=  1.550634765625
jika f(b)*f(x) < 0 maka a = x, b=  1.5504638671875
jika f(a)*f(x) < 0 maka b = x, b=  1.5505493164062498
x= 1.5505493164062498"""