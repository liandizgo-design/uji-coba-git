#password otomatis
import string
import secrets
import random

def buat_password(panjang: int) -> str:
    if panjang <= 0:
        raise ValueError("Panjang harus > 0")

    huruf_kecil = string.ascii_lowercase
    huruf_besar = string.ascii_uppercase
    angka = string.digits
    simbol = string.punctuation

    semua = huruf_kecil + huruf_besar + angka + simbol

    if panjang < 4:
        return ''.join(secrets.choice(semua) for _ in range(panjang))

    password_chars = [
        secrets.choice(huruf_kecil),
        secrets.choice(huruf_besar),
        secrets.choice(angka),
        secrets.choice(simbol),
    ]

    for _ in range(panjang - 4):
        password_chars.append(secrets.choice(semua))

    random.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)

def main():
    try:
        n = int(input("Masukkan panjang password: "))
    except ValueError:
        print("Masukkan angka bulat.")
        return

    if n <= 0:
        print("Panjang harus lebih dari 0.")
        return

    pwd = buat_password(n)
    print("Password terbuat:", pwd)

if __name__ == "__main__":
    main()
