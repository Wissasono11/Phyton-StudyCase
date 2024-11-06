def hitung_jarak():
    v = float(input("Masukkan kecepatan : "))
    t = float(input("Masukkan waktu     : "))
    s = v * t
    print("jarak yang ditempuh: ", s, "\n")

def hitung_kecepatan():
    s = float(input("Masukkan jarak : "))
    t = float(input("Masukkan waktu : "))
    v = s / t
    print("kecepatan yang ditempuh: ", v, "\n")

def hitung_waktu():
    s = float(input("Masukkan jarak : "))
    v = float(input("Masukkan kecepatan     : "))
    t = s / v
    print("waktu yang ditempuh: ", t, "\n")

while True:
    userInput = int(input(
        "Pilih rumus yang ingin digunakan : \n 1.hitung jarak\n 2.hitung kecepatan\n "
        "3.hitung waktu\n 0.selesai\nPilih nomor berapa:"))

    if(userInput == 1):
        hitung_jarak()
    elif (userInput == 2):
        hitung_kecepatan()
    elif (userInput == 3):
        hitung_waktu()
    else:
        break
