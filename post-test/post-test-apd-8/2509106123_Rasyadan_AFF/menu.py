from game_op import show, add, edit, delete
from auth import add_account
from next import clear

def menu_admin():
    while True:
        print("[1]Lihat daftar game\n[2]Tambah game\n[3]Edit game\n[4]Hapus game\n[5]Tambah akun\n[0]Logout")
        menu = input("Pilih menu: ")
        while not menu.isdigit():
            menu = input("Pilih 0-5: ")
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
            menu = input("Pilih 0/1: ")
        menu = int(menu)
        clear()

        if menu == 1:
            show()
        elif menu == 0:
            print("Logout berhasil")
            break