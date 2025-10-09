print("Misi Pertama")
stamina = int(input("stamina berdasarkan tiga digit nim terakhir: "))
print("=" *50)

cakra = 0
coba = 0

while cakra < 200 and stamina > 0:
    cakra += 5
    stamina -= 3
    coba += 1

print("Penyempurnaan Rasengan" .center(50))
print("=" *50)
print(f"Percobaan             : {coba}")
print(f"Jumlah cakra          : {cakra}")
print(f"Stamina               : {stamina}")
print("-" *50)
if cakra == 200 :
    print("\nNaruto berhasil mengumpulan 200 cakra!!")
else:
    print("\nNaruto gagal mengumpulan 200 cakra!!")
print("=" *50)

print("\nMisi Kedua")
meanra = int(input("tinggi menara berdasarkan 2 digit nim terakhir: "))
print("=" *50)

jum = 0

for i in range(1, meanra+1, 3):
    jum += 1
    print(f"\nNaruto bertemu gulungan")
print("=" *50)
print(f"\ngulungan informasi yang ia dapatkan: {jum}")

print("Misi Ketiga")
koridor = int(input("jumlah koridor berdasarkan digit terakhir kedua: "))
print("=" *50)

itn = 0
trap = 0

for j in range(1, koridor+1):
    print(f"\nKoridor {j}: ")
    print("-" *50)
    for k in range(1, 4):
        if k % 2 == 1:
            print(f"ruangan {k} berisi Data Intelijen")
            itn += 1
        else:
            print(f"ruangan {k} berisi Perangkap Peledak")
            trap += 1

print("=" *50)
print(f"Data intelijen yang didapatkan             : {itn}")
print(f"Perangkap Peledak yang berhasil dijinakkan : {trap}")