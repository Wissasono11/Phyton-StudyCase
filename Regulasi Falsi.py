def f(x):
    return (x+1)**2*(2.71823**(x**2-2))-1

error = 0.0001
a = 0.4
b = 1.2

def regulasi_falsi(a,b):
    i=0
    max_iter = 50
    iteration = True
    while iteration and i < max_iter:
        if f(a)*f(b) < 0:
            x = (a*abs(f(b)) + b*abs(f(a))) / (abs(f(a)) + abs(f(b)))
            if f(a)*f(x) < 0:
                b = x
                print("Jika f(a) x f(x) < 0 , maka b = x , b = ",x)
            if f(x)*f(b) < 0:
                a = x
                print("Jika f(b) x f(x) < 0 , maka a = x , a = ",x)
            if abs(a-b) < error:
                iteration = False
            else:
                i+=1
        else:
            print('tidak di temukan akar')
    print('x =', x)


regulasi_falsi(a,b)