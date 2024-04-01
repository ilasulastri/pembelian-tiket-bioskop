# Daftar film beserta harganya
daftar_film = {
    "Avengers: Endgame": 12,
    "Joker": 10,
    "Spider-Man: Far From Home": 10,
    "Toy Story 4": 8,
    "The Lion King": 9
}

# Input informasi pembeli
nama_pembeli = input("Masukkan nama Anda: ")
umur_pembeli = int(input("Masukkan umur Anda: "))
genre_film = input("Masukkan genre film yang Anda inginkan: ")

# Menampilkan daftar film sesuai genre yang dimasukkan
print("Daftar film yang tersedia:")
for judul, harga in daftar_film.items():
    if genre_film.lower() in judul.lower():
        print(f"{judul} - Harga: ${harga}")

# Memilih film
judul_film = input("Masukkan judul film yang ingin Anda tonton: ")
jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin Anda beli: "))

# Menghitung total harga tiket
if judul_film in daftar_film:
    harga_tiket = daftar_film[judul_film] * jumlah_tiket
    print(f"Total harga tiket untuk {jumlah_tiket} tiket film {judul_film}: ${harga_tiket}")
else:
    print("Maaf, judul film yang Anda masukkan tidak tersedia.")

# Menentukan diskon berdasarkan umur
if umur_pembeli < 13:
    diskon = 0.5  # Diskon 50% untuk anak-anak
elif umur_pembeli >= 65:
    diskon = 0.2  # Diskon 20% untuk lanjut usia
else:
    diskon = 0

# Menghitung total harga setelah diskon
harga_setelah_diskon = harga_tiket * (1 - diskon)
print(f"Total harga setelah diskon: ${harga_setelah_diskon}")

# Output
print(f"Terima kasih atas pembelian Anda, {nama_pembeli}! Selamat menonton film {judul_film}.")