# Program menghitung luas dan keliling
# Persegi, Persegi Panjang, dan Segitiga

def persegi():
    s = float(input("Masukkan sisi: "))
    print("Luas =", s*s)
    print("Keliling =", 4*s)

def persegipanjang():
    p = float(input("Masukkan panjang: "))
    l = float(input("Masukkan lebar: "))
    print("Luas =", p*l)
    print("Keliling =", 2*(p+l))

def segitiga():
    a = float(input("Masukkan alas: "))
    t = float(input("Masukkan tinggi: "))
    s1 = float(input("Masukkan sisi 1: "))
    s2 = float(input("Masukkan sisi 2: "))
    s3 = float(input("Masukkan sisi 3: "))
    print("Luas =", 0.5*a*t)
    print("Keliling =", s1+s2+s3)

while True:
    print("\n=== MENU ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Keluar")
    
    pilih = input("Pilih (1-4): ")
    
    if pilih == "1":
        persegi()
    elif pilih == "2":
        persegipanjang()
    elif pilih == "3":
        segitiga()
    elif pilih == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan salah!")
