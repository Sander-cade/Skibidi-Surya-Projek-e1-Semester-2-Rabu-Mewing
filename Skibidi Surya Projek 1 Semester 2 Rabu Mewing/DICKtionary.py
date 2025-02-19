data_siswa = {
    "nama" : "Surya Akbar A",
    "usia" : 12,
    "kelas" : "7 AE 4",
    "sekolah" : "Al-Wildan 3"
}
print ("Data lengkap siswa =", data_siswa)

nama = data_siswa["nama"]
print(nama)

data_siswa["alamat"] = "Tangerang Selatan"
print ("Data setelah menambah alamat adalah", data_siswa)

data_siswa["kelas"] = "8 AE 4"
print ("Data setelah update kelas adalah", data_siswa)

sekolah = data_siswa.pop("sekolah")
print ("Setelah data sekolah dihapus menjadi", data_siswa)