#   x  =   kelas utama
#   y  =   kelas ekonomi
# persamaan 1 >>> x + y = 860
# persamaan 2 >>> 25x + 10y = 13.400 atau 25000x + 10000y = 13.4 juta

#===========================#
# Program SPLDV Versi Manual#
#===========================#

#input
print("======Kelompok 18======")
print("1.Bayu Wicaksono \n2.Salman Alfauzi Asngari")
print("=======================")
print("Persamaan 1: ax + by = c")
print("Masukkan nilai variable :")
a = float(input("masukkan nilai a :"))
b = float(input("masukkan nilai b :"))
c = float(input("masukkan nilai c :"))

print("Persamaan 2: px + qy = r")
print("Masukkan nilai variable :")
p = float(input("masukkan nilai p : "))
q = float(input("masukkan nilai q : "))
r = float(input("masukkan nilai r : "))

#proses
x = (c*q-r*b)/(a*q-p*b)
y = (1/b)*(c-a*x)

#output
print("")
print("Solusi SPLDV : ")
print("x: ", x)
print("y: ", y)

