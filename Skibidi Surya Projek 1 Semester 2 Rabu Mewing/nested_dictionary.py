#Nested Dictionary (Dictionary di dalam dictionary)
data_siswa = {
    "siswa1" : {
        "nama" : "Surya Akbar",
        "kelas" : "7 AE 4",
        "usia" : 12,
        "alamat" : "Twin Tower"
    },
     "siswa2" : {
        "nama" : "Arga Dipta P",
        "kelas" : "8 AE 2",
        "usia" : 15,
        "alamat" : "Bandung"
    },
     "siswa3" : {
        "nama" : "Dzikraa Dungu",
        "kelas" : "7 AE 4",
        "usia" : 60,
        "alamat" : "Skibidi Toilet"
    }
}
print (data_siswa)

print (data_siswa["siswa2"])

print (data_siswa["siswa2"]["nama"])