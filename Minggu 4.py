# Program mencetak bilangan ganjil

# Input
N = int(input("Masukkan bilangan bulat: "))

# Loop mundur dari N ke 1
for i in range(N, 0, -1):
    if i % 2 != 0:  # cek ganjil
        print(i, end=" ")
