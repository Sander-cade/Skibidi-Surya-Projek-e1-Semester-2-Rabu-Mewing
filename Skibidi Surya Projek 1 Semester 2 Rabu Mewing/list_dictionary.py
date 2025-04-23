#List Dictionary
data_mobil = [
    {
        "nama_mobil" : "Osama",         #Ini indeks 0
        "merek" : "bin Laden",
        "tahun" : 2001
        },
    {
        "nama_mobil" : "Adolf",         #Ini indeks 1
        "merek" : "Hitler",
        "tahun" : 1943
        },
    {
        "nama_mobil" : "Prabowo",       #Ini indeks 2
        "merek" : "Makan Sinag",
        "tahun" : 2025
        },
]
print (data_mobil)

mobil1 = data_mobil[1]  #-----
print (mobil1)          #cara 1

print (data_mobil[1]) #cara 2

#menambah data mobil baru
mobil_baru = {"nama_mobil" : "Skibidi",
              "merek" : "Toilet",
              "Tahun" : 2023}
data_mobil.append (mobil_baru)
print (data_mobil)

#Menghapus data mobil baru berdasarkan dari indeksnya
data_mobil.pop (1)
print (data_mobil)