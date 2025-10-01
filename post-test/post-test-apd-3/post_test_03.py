print("\npenghitung gaji karyawan PT. BOM")
print("=" * 50)


jabatan_stock = {
    1: "peracik",
    2: "pengantar"
}


nama = input("Nama: ")

while True:
    try:
        pilih = int(input("Pilih jabatan (1.peracik, 2.pengantar): "))
        if pilih in jabatan_stock:
            jabatan = jabatan_stock[pilih]
            break
        else:
            print("pilihan tidak sesuai!! silahkan masukan ulang")
    except ValueError:
        print("input salah!! silahkan pilih 1/2")

hari = int(input("Hari kerja: "))
jam_kerja = int(input("Jam kerja: "))
jum_lembur = int(input("Jam lembur: "))

if pilih == 1:
    if hari >= 24 and jam_kerja >= 8 and jum_lembur >= 4:
        bayar_jam = 25000
        bayar_lembur = 15000
    elif hari >= 18 and jam_kerja >= 6 and jum_lembur >= 2:
        bayar_jam = 20000
        bayar_lembur = 10000
    else:
        bayar_jam = 15000
        bayar_lembur = 10000
elif pilih == 2:
    if hari >= 20 and jam_kerja >= 7 and jum_lembur >= 7:
        bayar_jam = 25000
        bayar_lembur = 20000
    elif hari >= 16 and jam_kerja >= 5 and jum_lembur >= 4:
        bayar_jam = 20000
        bayar_lembur = 15000
    else:
        bayar_jam = 15000
        bayar_lembur = 12000
else:
    print("tidak ada jabatan")

total = ((bayar_jam * jam_kerja) * hari) + (bayar_lembur * jum_lembur)

print("\ndata gaji karyawan PT. BOM")
print("=" * 50)
print(f"nama             : {nama}")
print(f"jabatan          : {jabatan}")
print(f"hari Kerja       : {hari}")
print(f"jam Kerja        : {jam_kerja}")
print(f"lembur           : {jum_lembur}")
print("-" * 50)
print(f"bayar perjam     :Rp{bayar_jam:,}")
print(f"bayar perlembur  :Rp{bayar_lembur:,}")
print(f"gaji             :Rp{total:,}")
