from menu import menu_admin, menu_user
from auth import login, register
from next import clear

while True:
    print("🎊 Welcome To GameKuDuniaku 🎊".center(80))
    print("=" * 80)
    print("[1]Login\n[2]Register\n[0]Keluar")

    pilih = input("Pilih menu: ")
    while not pilih.isdigit():
        pilih = input("Input harus angka: ")
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