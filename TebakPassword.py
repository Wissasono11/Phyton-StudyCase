def tebakPassword(benar):
    # Mencoba semua kemungkinan kombinasi 3 digit
    for digit1 in range(10):          # 0-9 untuk digit pertama
        for digit2 in range(10):      # 0-9 untuk digit kedua
            for digit3 in range(10):  # 0-9 untuk digit ketiga
                # Membuat kombinasi password
                tebakan = f"{digit1}{digit2}{digit3}"
                
                print(f"Mencoba: {tebakan}")
                
                # Memeriksa apakah password cocok
                if tebakan == benar:
                    return f"Password ditemukan: {tebakan}"
                
    return "Password tidak ditemukan"

# Contoh penggunaan
value = tebakPassword("1234")
print(value)