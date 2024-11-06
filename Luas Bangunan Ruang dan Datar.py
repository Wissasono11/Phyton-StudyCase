
def hitung_kecepatan():
    print("hitung kecepatan ready💩")
    jarak = float(input("masukkan jarak: "))
    waktu = float(input("masukkan waktu: "))
    kecepatan = jarak * waktu
    print("kecepatan: ", kecepatan, "\n")

def luas_segitiga():
    print("hitung segitiga ⚠️")
    alas = float(input("masukkan alas: "))
    tinggi = float(input("masukkan tinggi: "))
    luas = 0.5 * (alas * tinggi)
    print("luas segitiga: ", luas, "\n")

def luas_balok():
    print("hitung balok 👌👌👌")
    panjang = float(input("masukkan panjang: "))
    lebar   = float(input("masukkan lebar: "))
    tinggi = float(input("masukkan tinggi: "))
    luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
    print("luas balok: ", luas, "\n")

def luas_bola():
    print("hitung bola 🏀")
    r = float(input("masukkan jari-jari: "))
    luas = 4 * 3.14 * (r**2)
    print("luas bola: ", luas, "\n")

while True:
    userInput = int(input(
        "pilih rumus yang ingin dipakai: \n\n1.hitung kecepatan\n2.luas segitiga\n3."
        "luas balok\n4.luas bola\n\n0.keluar program\n\npilih nomor berapa: "))

    if(userInput == 1):
        hitung_kecepatan()
    elif(userInput == 2):
        luas_segitiga()
    elif(userInput == 3):
        luas_balok()
    elif(userInput == 4):
        luas_bola()
    else:
        break
