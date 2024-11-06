import string

def tebakPassword(benar):
    # Definisikan semua karakter alfanumerik
    karakter = string.digits + string.ascii_letters
    
    for char1 in karakter:
        for char2 in karakter:
            for char3 in karakter:
                for char4 in karakter:
                    for char5 in karakter:
                        # Membuat kombinasi password
                        tebakan = f"{char1}{char2}{char3}{char4}{char5}"
                        
                        print(f"Mencoba: {tebakan}")
                        
                        # Memeriksa apakah password cocok
                        if tebakan == benar:
                            return f"Password ditemukan: {tebakan}"
                        
    return "Password tidak ditemukan"

# Contoh penggunaan
value = tebakPassword("a1B2c")
print(value)