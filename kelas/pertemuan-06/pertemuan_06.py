# buah = {"apel", "jeruk", "mangga", "apel"}
# print(buah)

# angka_ganjil = {1, 3, 5, 7, 9}

# for angka in angka_ganjil:
#     print(angka)

# add
# angka_ganjil.add(11)
# print(angka_ganjil)

# rm
# angka_ganjil.remove(9)
# angka_ganjil.discard(9)
# print(angka_ganjil)

# dictionary
Biodata = {
"Nama" : "Ananda Daffa Harahap",
"NIM" : 2409106050,
"KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
"Mahasiswa_Aktif" : True,
"Social Media" : {
"Instagram" : "daffahrhap"
}
}

# print(Biodata.get("NIM"))
# print(Biodata["NIM"])

# loop
# for i in Biodata:
#     print(i)
# print("")
# for i, j in Biodata.items():
#     print(f"out {i} anda adalah {j}")

# update
# Biodata["Nama"] = "jamal"
# Biodata.update({"Nama" : "Jamal"})
# print(Biodata.get("Nama"))

# call nested dictionary
# print(Biodata["Social Media"] ["Instagram"])

# del
# del Biodata["Nama"]
# print(Biodata["Nama"])

# pop
# simpan = Biodata.pop("Nama")
# print(Biodata["Nama"])
# print(simpan)

# clear
# Biodata.clear()
# print(Biodata)

# len
# print("ini len", len(Biodata))

# copy
# coba = {
#     "nama" : "jamal",
#     "suku" : "jawa"
# }

# salin = coba.copy()
# print(f"salin {salin}")

# key/value
# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #menggunakan keys
# for i in Nilai.keys():
# print(i)
# print("")
# #menggunakan value
# for i in Nilai.values():
# print(i)

# setdefault
# print("ini setdefault", Biodata.setdefault("Nama2", "jamal"))
