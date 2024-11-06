def convert_length():
    print("\nPilih konversi panjang:")
    print("1. Meter ke Kilometer")
    print("2. Kilometer ke Meter")
    print("3. Meter ke Sentimeter")
    print("4. Sentimeter ke Meter")
    choice = int(input("Masukkan pilihan: "))
    value = float(input("Masukkan nilai: "))

    if choice == 1:
        result = value / 1000
        print(f"{value} meter = {result} kilometer")
    elif choice == 2:
        result = value * 1000
        print(f"{value} kilometer = {result} meter")
    elif choice == 3:
        result = value * 100
        print(f"{value} meter = {result} sentimeter")
    elif choice == 4:
        result = value / 100
        print(f"{value} sentimeter = {result} meter")
    else:
        print("Pilihan tidak valid")


def convert_mass():
    print("\nPilih konversi massa:")
    print("1. Kilogram ke Gram")
    print("2. Gram ke Kilogram")
    print("3. Kilogram ke Ton")
    print("4. Ton ke Kilogram")
    choice = int(input("Masukkan pilihan: "))
    value = float(input("Masukkan nilai: "))

    if choice == 1:
        result = value * 1000
        print(f"{value} kilogram = {result} gram")
    elif choice == 2:
        result = value / 1000
        print(f"{value} gram = {result} kilogram")
    elif choice == 3:
        result = value / 1000
        print(f"{value} kilogram = {result} ton")
    elif choice == 4:
        result = value * 1000
        print(f"{value} ton = {result} kilogram")
    else:
        print("Pilihan tidak valid")


def convert_temperature():
    print("\nPilih konversi suhu:")
    print("1. Celsius ke Fahrenheit")
    print("2. Fahrenheit ke Celsius")
    choice = int(input("Masukkan pilihan: "))
    value = float(input("Masukkan nilai: "))

    if choice == 1:
        result = (value * 9/5) + 32
        print(f"{value} derajat Celsius = {result} derajat Fahrenheit")
    elif choice == 2:
        result = (value - 32) * 5/9
        print(f"{value} derajat Fahrenheit = {result} derajat Celsius")
    else:
        print("Pilihan tidak valid")


def main():
    while True:
        print("\nKonversi Satuan Internasional")
        print("1. Konversi Panjang")
        print("2. Konversi Massa")2
        print("3. Konversi Suhu")
        print("4. Keluar")
        choice = int(input("Masukkan pilihan: "))

        if choice == 1:
            convert_length()
        elif choice == 2:
            convert_mass()
        elif choice == 3:
            convert_temperature()
        elif choice == 4:
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
