#input
nama = str(input("Nama penyewa hotel: "))
lama = int(input("Lama menginap: "))
print("Jenis kamar yang tersedia\n 1. Deluxe\n 2. Superior\n 3. Superior Grand Deluxe")
jenis = int(input("Jenis kamar yang dipilih: "))
member = input("Kartu member: ")
print("=======================")
print("Tuan/Nyonya", nama)

#deklarasi harga

deluxe = 300000
superior = 500000
superior_grand_deluxe = 1000000  

#menghitung harga yang ditetapkan
if jenis == 1:
   harga = deluxe
elif jenis == 2:
   harga = superior
elif jenis == 3:
   harga = superior_grand_deluxe
else:
   print("Jenis kamar tidak valid. Mohon pilih kembali.")
   exit()

total = harga * lama

#menghitung diskon
if member.lower() == "ya":
   diskon = 0.10 * total
   total -= diskon

#output
print(f"Anda memilih kamar jenis, {jenis} untuk tinggal selama, {lama} hari.")
print(f"Harga kamar per malam adalah Rp.{harga}")
print(f"Selamat anda mendapatkan diskon sebesar 10%")
print(f"Total bayar Rp.{total}")