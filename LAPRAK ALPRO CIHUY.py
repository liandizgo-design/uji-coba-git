print("="*40)
print("       Chatbot Sederhana Python")
print("="*40)
print("Ketik 'exit' untuk mengakhiri percakapan\n")

while True:
    user = input("Anda : ")
    
    # keluar jika user mengetik 'exit'
    if user.lower() == "exit":
        print("Chatbot : Terima kasih sudah mengobrol 😊")
        break
    
    # Respon sederhana (aturan dasar)
    elif "halo" in user.lower():
        print("Chatbot : Halo juga! Apa kabar?")
    elif "apa kabar" in user.lower():
        print("Chatbot : Aku baik, terima kasih. Kamu gimana?")
    elif "siapa kamu" in user.lower():
        print("Chatbot : Aku chatbot sederhana yang kamu buat.")
    elif "hitung" in user.lower():
        print("Chatbot : Kalau mau hitung, coba kasih aku angka 😊")
    else:
        print("Chatbot : Maaf, aku belum mengerti itu.")
