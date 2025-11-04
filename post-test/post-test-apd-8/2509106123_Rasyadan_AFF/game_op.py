from data import game
from next import nxt
from prettytable import PrettyTable


def show(pause=True):
    print("Daftar game")
    print("-" * 80)
    if not game:
        print("Belum ada Game")
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama", "Genre", "Tahun"]
        for j, (k, l) in enumerate(game.items()):
            table.add_row([
                j + 1,
                k,
                l["genre"],
                l["tahun"]
            ])
        print(table)
    if pause:
        nxt()

def add():
    print("Tambah game")
    print("-" * 80)
    nama = input("Nama game: ")
    genre = input("Genre: ")
    tahun = input("Tahun rilis: ")

    if not nama.strip() or not genre.strip() or not tahun.isdigit():
        print("Input tidak sesuai!")
    else:
        game[nama] = {"genre": genre, "tahun": tahun}
        print(f"Game {nama} berhasil ditambah")
    nxt()

def edit():
    print("Edit game")
    print("-" * 80)
    if not game:
        print("Belum ada Game")
        nxt()
        return
    show(pause=False)
    pilih = input("\nPilih No game: ")
    while not pilih.isdigit() or int(pilih) not in range(1, len(game)+1):
        pilih = input("Pilih nomor yang sesuai: ")

    index = int(pilih) - 1
    nama_lama = list(game.keys())[index]

    nama = input("Nama baru (kosongkan jika tidak diubah): ")
    genre = input("Genre baru (kosongkan jika tidak diubah): ")
    tahun = input("Tahun baru (kosongkan jika tidak diubah): ")

    if nama.strip():
        game[nama] = game.pop(nama_lama)
        nama_lama = nama
    if genre.strip():
        game[nama_lama]["genre"] = genre
    if tahun.isdigit():
        game[nama_lama]["tahun"] = tahun

    print("Data berhasil diupdate")
    nxt()

def delete():
    print("Hapus game")
    print("-" * 80)
    if not game:
        print("Belum ada Game")
        nxt()
        return

    show(pause=False)
    pilih = input("\nPilih No game: ")
    while not pilih.isdigit() or int(pilih) not in range(1, len(game)+1):
        pilih = input("Pilih nomor yang sesuai: ")

    index = int(pilih) - 1
    hapus = list(game.keys())[index]
    del game[hapus]
    print(f"Berhasil hapus {hapus}")
    nxt()