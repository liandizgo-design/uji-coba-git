# Program menghitung faktorial dengan penjabaran

n = int(input("Masukkan bilangan: "))

faktorial = 1
penjabaran = ""

for i in range(n, 0, -1):
    faktorial *= i
    if i == 1:
        penjabaran += str(i)
    else:
        penjabaran += str(i) + " x "

print(f"{n}! = {penjabaran} = {faktorial}")
