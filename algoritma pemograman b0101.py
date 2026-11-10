# dekrelarasi variabel sederhana
nama_depan = "budi"
umur = 20
tinggi_badan = 170.5
is_aktif = True

# menampilkan nilai variabel
print("Nama Depan:", nama_depan)
print("Umur:", umur, "tahun")
print("Tinggi Badan:", tinggi_badan, "cm")
print("Apakah Aktif:", is_aktif)

#deklerasi berbagai tipe data dasar
angka_bulat = 25
angka_desimal = 3.14
teks = "belajar Python"
status = False

#menegenalkan tipe data masing-masing variabel
print("Tipe data angka_bulat:", type(angka_bulat))
print("Tipe data angka_desimal:", type(angka_desimal))
print("Tipe data teks:", type(teks))
print("Tipe data status:", type(status))

# list (berurutan, bisa diubah / mutable)
hobi = ["membaca", "mengoding", "berenang"]
print("Hobi:", hobi)
print("Tipe data hobi:", type(hobi))

#tuple (berurutan, tidak bisa diubah / immutable)
koordinat = (-6,1751, 106.8650)
print ("tuple koordinat:", koordinat)
print("Tipe data koordinat:", type(koordinat))

# DICTIONARY (PASANGAN KEY DAN VALUE
mahasisswa = {
    
    "nama": "siti",
    "nim": 123456,
    "ipk": 3.85
}
print("dict mahasiswa:", mahasisswa)
print("Tipe data mahasiswa:", type(mahasisswa))

#set (nilai unik, tidak berurutan, tidak duplikat)
angka_unik = {1, 2, 2, 3, 4, 4, 5}
print("set angka unik (otomatis menghapus duplikat):", angka_unik)
print("Tipe data angka_unik:", type(angka_unik))

# konverensi dari string ke integer
str_angka = "100"
int_angka = int(str_angka)
print("hasil penjumlahan (100 + 50):", int_angka + 50)

#konverensi dari float ke INTEGER KE STRING
ipk_float = 3.75
ipk_int = int(ipk_float)
print("float ke int:", ipk_int)

#konverensi dari integer ke string
tahun = 2024
pesan = "tahun saat ini: " + str(tahun)
print(pesan)

#konverensi dari list ke set (menghapus elemen duplikat)
daftar_buah = ["apel", "jeruk", "apel", "pisang", "jeruk"]
daftar_buah_unik = set(daftar_buah)
print("daftar buah unik:", daftar_buah_unik)