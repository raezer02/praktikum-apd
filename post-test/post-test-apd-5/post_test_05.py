# post_5
import os

os.system('cls || clear')

akun = [
    ["etmin", "god", "admin"],
    ["rakyat", "nigen", "user"]
]

game = [
    ["Roblox", "Game", "2007"],
    ["Mobilegend", "Moba", "2006"]
]

while True:
    print("🎊🎊Welcome To GameKuDuniaku🎊🎊".center(50))
    print("=" *50)
    print("[1]Login\n[2]Register\n[0]Keluar")
    
    pilih = input("Pilih menu: ")
    while not pilih.isdigit():
        pilih = input("Input tidak sesuai! Pilih 1, 2, atau 0: ")
    
    pilih = int(pilih)
    os.system('cls || clear')

    if pilih == 1:
        print("LOGIN")
        print("-" *50)
        username = input("Username: ")
        password = input("Password: ")

        role = None
        for i in akun:
            if i[0] == username and i[1] == password:
                role = i[2]
                break
        if role is None:
            print("ada yang salah di bagian username atau password")
            print("-" *50)
            input("tekan enter untuk lanjut...")
            os.system('cls || clear')
            continue

        print(f"Login berhasil sebagai {role.capitalize()}\n")
        print("-" *50)


        if role == "admin":
            while True:
                print("[1]Lihat daftar game\n[2]Tambah game\n[3]Edit game\n[4]Hapus game\n[5]Tambah akun\n[0]Logout")
                menu_admin = input("Pilih menu: ")

                while not menu_admin.isdigit():
                    menu_admin = input("Input tidak sesuai! Pilih 0-5: ")
                menu_admin = int(menu_admin)
                os.system('cls || clear')

                if menu_admin == 1:
                    print("Daftar game")
                    if len(game) == 0:
                        print("Belum ada Game")
                    else:
                        for j, k in enumerate(game):
                            print("-" *80)
                            print(f"{j+1:<3} | Nama: {k[0]:<15} | Genre: {k[1]:<10} | Tahun: {k[2]:<5}")
                            print("-" *80)
                    input("\ntekan enter untuk lanjut...")
                    # os.system('cls || clear')

                elif menu_admin == 2:
                    print("Tambah game")
                    print("-" *50)
                    nama = input("Nama game: ")
                    genre = input("Genre: ")
                    tahun = input("Tahun rilis: ")

                    if nama.strip() == "" or genre.strip() == "" or not tahun.isdigit():
                        print("-" *50)
                        print("Input tidak sesuai!")
                    else:
                        game.append([nama, genre, tahun])
                        print("-" *50)
                        print(f"Game {nama} berhasil di tambah")
                    input("\ntekan enter untuk lanjut...")
                    os.system('cls || clear')

                elif menu_admin == 3:
                    print("Edit game")
                    if len(game) == 0:
                        print("Belum ada Game")
                        input("\ntekan enter untuk lanjut...")
                        os.system('cls || clear')
                        continue

                    for j, k in enumerate(game):
                        print("-" *50)
                        print(f"{j+1:<3}. {k[0]:<15} | {k[1]:<10} | {k[2]:<5}")
                        print("-" *50)

                    pilih_edit = input("\nPilih No game yang ingin di edit: ")
                    print("-" *50)
                    while not pilih_edit.isdigit() or int(pilih_edit) < 1 or int(pilih_edit) > len(game):
                        pilih_edit = input("Input tidak sesuai pilih no game: ")

                    index = int(pilih_edit) - 1
                    nama = input("Nama baru (kosongkan jika tidak diubah): ")
                    genre = input("Genre baru (kosongkan jika tidak diubah): ")
                    tahun = input("Tahun baru (kosongkan jika tidak diubah): ")

                    if nama.strip() != "":
                        game[index][0] = nama
                    if genre.strip() != "":
                        game[index][1] = genre
                    if tahun.isdigit():
                        game[index][2] = tahun

                    print("-" *50)
                    print("Data berhasil di update")
                    input("\ntekan enter untuk lanjut...")
                    os.system('cls || clear')

                elif menu_admin == 4:
                    print("Hapus game")
                    if len(game) == 0:
                        print("Belum ada Game")
                        input("\ntekan enter untuk lanjut...")
                        os.system('cls || clear')
                        continue

                    for j, k in enumerate(game):
                        print("-" *50)
                        print(f"{j+1:<3}. {k[0]:<15} | {k[1]:<10} | {k[2]:<5}")
                        print("-" *50)

                    pilih_hapus = input("\nPilih No game yang ingin di hapus: ")
                    while not pilih_hapus.isdigit() or int(pilih_hapus) < 1 or int(pilih_hapus) > len(game):
                        pilih_hapus = input("Input tidak sesuai pilih no game: ")

                    index = int(pilih_hapus) - 1
                    hapus = game[index][0]
                    del game[index]
                    print("-" *50)
                    print(f"Berhasil hapus {hapus}")
                    input("\ntekan enter untuk lanjut...")
                    os.system('cls || clear')

                elif menu_admin == 5:
                    print("Tambah akun")
                    print("-" *50)
                    username = input("Buat user name: ")


                    check = False
                    for a in akun:
                        if a[0] == username:
                            check = True
                            break

                    if check:
                        print("Nama sudah di pakai, gunakan nama lain")
                    else:
                        password = input("Buat password: ")

                        print("\nPilih role:")
                        print("[0]Admin\n[1]User")
                        pilih_role = input(": ")
                        while not pilih_role.isdigit() or int(pilih_role) not in [0, 1]:
                            pilih_role = input("Input tidak sesuai, silahkan pilih 0/1: ")
                        
                        role = "admin" if int(pilih_role) == 0 else "user"
                        akun.append([username, password, role])
                        print("-" *50)
                        print(f"Akun {username} berhasil di buat sebagai {role}")
                    
                    input("\ntekan enter untuk lanjut...")
                    os.system('cls || clear')
                    
                elif menu_admin == 0:
                    print("Logout berhasil")
                    break
                else:
                    print("Pilihan tidak tersedia!")
                    input("\ntekan enter untuk lanjut...")
                    os.system('cls || clear')


        elif role == "user":
            while True:
                print("[1]Lihat daftar game\n[0]Logout")
                user_menu = input("Pilih menu: ")
                while not user_menu.isdigit():
                    user_menu = input("Input tidak sesuai pilih 0/1")
                user_menu = int(user_menu)
                os.system('cls || clear')
                
                if user_menu == 1:
                    print("Daftar game")
                    if len(game) == 0:
                        print("Belum ada Game")
                    else:
                        for j, k in enumerate(game):
                            print("-" *80)
                            print(f"{j+1:<3} | Nama: {k[0]:<15} | Genre: {k[1]:<10} | Tahun: {k[2]:<5}")
                            print("-" *80)
                    # input("\ntekan enter untuk lanjut...")
                    

                elif user_menu == 0:
                    print("Logout berhasil")
                    break
                else:
                    print("Pilihan tidak tersedia!")
                    input("\ntekan enter untuk lanjut...")
                    os.system('cls || clear')


    elif pilih == 2 :
        print("REGISTER")
        print("-" *50)
        username = input("Buat user name: ")

        check = False
        for a in akun:
            if a[0] == username:
                check = True
                break
        
        if check:
            print("Nama sudah di pakai, gunakan nama lain")
        else:
            password = input("Buat password: ")

            role = "user"
            akun.append([username, password, role])
            print(f"Akun {username} berhasil di buat")
        input("\ntekan enter untuk lanjut...")
        os.system('cls || clear')
    else:
        break
    print("anda berhasil keluar")