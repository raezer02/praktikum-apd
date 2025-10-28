import os

os.system('cls || clear')

akun = {
    "admin": [{"username": "etmin", "password": "god", "role": "admin"}],
    "user": [{"username": "rakyat", "password": "nigen", "role": "user"}]
}

game = {
    "Roblox": {"genre": "game", "tahun": "2007"},
    "Mobilegend": {"genre": "Moba", "tahun": "2006"}
}


def clear():
    os.system('cls || clear')


def nxt():
    input("\ntekan enter untuk lanjut...")
    clear()


def show(pause=True):
    print("Daftar game")
    print("-" * 80)
    if not game:
        print("Belum ada Game")
    else:
        for j, (k, l) in enumerate(game.items()):
            print(f"{j + 1:<3} | Nama: {k:<15} | Genre: {l['genre']:<10} | Tahun: {l['tahun']:<5}")
            print("-" * 80)
    if pause:
        nxt()


def username_exists(username):
    for role_list in akun.values():
        for a in role_list:
            if a["username"] == username:
                return True
    return False


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
    pilih_edit = input("\nPilih No game yang ingin di edit: ")
    while not pilih_edit.isdigit() or int(pilih_edit) not in range(1, len(game) + 1):
        pilih_edit = input("Input tidak sesuai pilih no game: ")

    index = int(pilih_edit) - 1
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
    pilih_hapus = input("\nPilih No game yang ingin dihapus: ")
    while not pilih_hapus.isdigit() or int(pilih_hapus) not in range(1, len(game) + 1):
        pilih_hapus = input("Input tidak sesuai pilih no game: ")

    index = int(pilih_hapus) - 1
    hapus = list(game.keys())[index]
    del game[hapus]
    print(f"Berhasil hapus {hapus}")
    nxt()


def add_account():
    print("Tambah akun")
    print("-" * 80)
    username = input("Buat user name: ")

    if username_exists(username):
        print("Nama sudah di pakai, gunakan nama lain")
    else:
        password = input("Buat password: ")

        print("\nPilih role:")
        print("[0]Admin\n[1]User")
        pilih_role = input(": ")
        while not pilih_role.isdigit() or int(pilih_role) not in [0, 1]:
            pilih_role = input("Input tidak sesuai, silahkan pilih 0/1: ")

        role = "admin" if int(pilih_role) == 0 else "user"

        akun[role].append({"username": username, "password": password, "role": role})
        print("-" * 80)
        print(f"Akun {username} berhasil di buat sebagai {role}")
    nxt()


def register():
    print("REGISTER")
    print("-" * 80)
    username = input("Buat user name: ")

    if username_exists(username):
        print("Nama sudah dipakai, gunakan nama lain")
    else:
        password = input("Buat password: ")
        akun["user"].append({"username": username, "password": password, "role": "user"})
        print(f"Akun {username} berhasil dibuat")
    nxt()


def login():
    print("LOGIN")
    print("-" * 80)
    username = input("Username: ")
    password = input("Password: ")

    for role, role_list in akun.items():
        for db in role_list:
            if db["username"] == username and db["password"] == password:
                print(f"Login berhasil sebagai {role.capitalize()}\n")
                print("-" * 80)
                return role
    print("Ada yang salah di bagian username atau password")
    nxt()
    return None


def menu_admin():
    while True:
        print("[1]Lihat daftar game\n[2]Tambah game\n[3]Edit game\n[4]Hapus game\n[5]Tambah akun\n[0]Logout")
        menu = input("Pilih menu: ")
        while not menu.isdigit():
            menu = input("Input tidak sesuai! Pilih 0-5: ")
        menu = int(menu)
        clear()

        if menu == 1:
            show()
        elif menu == 2:
            add()
        elif menu == 3:
            edit()
        elif menu == 4:
            delete()
        elif menu == 5:
            add_account()
        elif menu == 0:
            print("Logout berhasil")
            break


def menu_user():
    while True:
        print("[1]Lihat daftar game\n[0]Logout")
        menu = input("Pilih menu: ")
        while not menu.isdigit():
            menu = input("Input tidak sesuai pilih 0/1: ")
        menu = int(menu)
        clear()

        if menu == 1:
            show()
        elif menu == 0:
            print("Logout berhasil")
            break


while True:
    print("🎊🎊Welcome To GameKuDuniaku🎊🎊".center(80))
    print("=" * 80)
    print("[1]Login\n[2]Register\n[0]Keluar")

    pilih = input("Pilih menu: ")
    while not pilih.isdigit():
        pilih = input("Input tidak sesuai! Pilih 1, 2, atau 0: ")
    pilih = int(pilih)
    clear()

    if pilih == 1:
        role = login()
        if role == "admin":
            menu_admin()
        elif role == "user":
            menu_user()

    elif pilih == 2:
        register()

    elif pilih == 0:
        print("Anda berhasil keluar")
        break
