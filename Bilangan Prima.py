a = int(input("Masukkan angka: "))
if(a == 2 or a == 3 or a == 5 or a == 7) or (a % 2 != 0 and a % 3 != 0 and a % 5 != 0 and a % 7 != 0):
    print(format(a), "adalah bilangan prima")
else:
    print(format(a), "bukan bilangan prima")