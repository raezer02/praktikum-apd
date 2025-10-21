import os

os.system('cls || clear')

akun = {
    "admin" : {"username" : "etmin", "password" : "god", "role" : "admin"},
    "user"  : {"username" : "rakyat","password" : "nigen", "role" : "user"}
}

game = {
    "Roblox" : {"genre" : "game", "tahun" : "2007"},
    "Mobilegend" : {"genre" : "Moba", "tahun" : "2006"}
}

while True:
    print("🎊🎊Welcome To GameKuDuniaku🎊🎊".center(80))
    print("=" *80)
    print("[1]Login\n[2]Register\n[0]Keluar")
    
    pilih = input("Pilih menu: ")
    while not pilih.isdigit():
        pilih = input("Input tidak sesuai! Pilih 1, 2, atau 0: ")
    
    pilih = int(pilih)
    os.system('cls || clear')

    if pilih == 1:  #done
        print("LOGIN")
        print("-" *80)
        username = input("Username: ")
        password = input("Password: ")

        role = None
        for key , db in akun.items():
            if db["username"] == username and db["password"] == password:
                role = key
                break
        if role is None:
            print("ada yang salah di bagian username atau password")
            print("-" *80)
            input("tekan enter untuk lanjut...")
            os.system('cls || clear')
            continue

        print(f"Login berhasil sebagai {role.capitalize()}\n")
        print("-" *80)

        if role == "admin":
            while True:
                print("[1]Lihat daftar game\n[2]Tambah game\n[3]Edit game\n[4]Hapus game\n[5]Tambah akun\n[0]Logout")
                menu_admin = input("Pilih menu: ")

                while not menu_admin.isdigit():
                    menu_admin = input("Input tidak sesuai! Pilih 0-5: ")
                menu_admin = int(menu_admin)
                os.system('cls || clear')

                if menu_admin == 1: #done
                    print("Daftar game")
                    print("-" *80)
                    if len(game) == 0:
                        print("Belum ada Game")
                    else:
                        for j, (k, l) in enumerate(game.items()):
                            # print("-" *80)
                            print(f"{j+1:<3} | Nama: {k:<15} | Genre: {l['genre']:<10} | Tahun: {l['tahun']:<5}")
                            print("-" *80)
                    input("\ntekan enter untuk lanjut...")
                    # os.system('cls || clear')

                elif menu_admin == 2:   #done
                    print("Tambah game")
                    print("-" *80)
                    nama = input("Nama game: ")
                    genre = input("Genre: ")
                    tahun = input("Tahun rilis: ")

                    if nama.strip() == "" or genre.strip() == "" or not tahun.isdigit():
                        print("-" *80)
                        print("Input tidak sesuai!")
                    else:
                        game.update({nama: {"genre": genre, "tahun": tahun}})
                        print("-" *80)
                        print(f"Game {nama} berhasil di tambah")
                    input("\ntekan enter untuk lanjut...")
                    os.system('cls || clear')

                elif menu_admin == 3:   #done
                    print("Edit game")
                    print("-"*80)
                    if len(game) == 0:
                        print("Belum ada Game")
                        input("\ntekan enter untuk lanjut...")
                        os.system('cls || clear')
                        continue
                    for j, (k, l) in enumerate(game.items()):
                            # print("-" *80)
                            print(f"{j+1:<3} | Nama: {k:<15} | Genre: {l['genre']:<10} | Tahun: {l['tahun']:<5}")
                            print("-" *80)

                    pilih_edit = input("\nPilih No game yang ingin di edit: ")
                    print("-" *80)
                    while not pilih_edit.isdigit() or int(pilih_edit) < 1 or int(pilih_edit) > len(game):
                        pilih_edit = input("Input tidak sesuai pilih no game: ")

                    index = int(pilih_edit) - 1
                    nama_lama = list(game.keys())[index]

                    nama = input("Nama baru (kosongkan jika tidak diubah): ")
                    genre = input("Genre baru (kosongkan jika tidak diubah): ")
                    tahun = input("Tahun baru (kosongkan jika tidak diubah): ")

                    if nama.strip() != "":
                        game[nama] = game.pop(nama_lama)
                        nama_lama = nama
                        # game[index][0] = nama
                    if genre.strip() != "":
                        game[nama]["genre"] = genre
                        # game[index][1] = genre
                    if tahun.isdigit():
                        game[nama]["tahun"] = tahun 
                        # game[index][2] = tahun

                    print("-" *80)
                    print("Data berhasil di update")
                    input("\ntekan enter untuk lanjut...")
                    os.system('cls || clear')

                elif menu_admin == 4:   #done
                    print("Hapus game")
                    print("-" *80)
                    if len(game) == 0:
                        print("Belum ada Game")
                        input("\ntekan enter untuk lanjut...")
                        os.system('cls || clear')
                        continue
                    for j, (k, l) in enumerate(game.items()):
                            # print("-" *80)
                            print(f"{j+1:<3} | Nama: {k:<15} | Genre: {l['genre']:<10} | Tahun: {l['tahun']:<5}")
                            print("-" *80)

                    pilih_hapus = input("\nPilih No game yang ingin di hapus: ")
                    while not pilih_hapus.isdigit() or int(pilih_hapus) < 1 or int(pilih_hapus) > len(game):
                        pilih_hapus = input("Input tidak sesuai pilih no game: ")

                    index = int(pilih_hapus) - 1
                    hapus = list(game.keys())[index]
                    # hapus = game[index][0]
                    del game[hapus]
                    print("-" *80)
                    print(f"Berhasil hapus {hapus}")
                    input("\ntekan enter untuk lanjut...")
                    os.system('cls || clear')

                elif menu_admin == 5:   #done
                    print("Tambah akun")
                    print("-" *80)
                    username = input("Buat user name: ")


                    check = False
                    for a in akun.values():
                        if a["username"] == username:
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

                        key_baru = role

                        akun.update({key_baru: {"username": username, "password": password}})
                        # akun[key_baru] = {"username": username, "password": password}
                        print("-" *80)
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
                
                if user_menu == 1:  #done
                    print("Daftar game")
                    print("-" *80)
                    if len(game) == 0:
                        print("Belum ada Game")
                    else:
                        for j, (k, l) in enumerate(game.items()):
                            # print("-" *80)
                            print(f"{j+1:<3} | Nama: {k:<15} | Genre: {l['genre']:<10} | Tahun: {l['tahun']:<5}")
                            print("-" *80)
                    # input("\ntekan enter untuk lanjut...")
                    

                elif user_menu == 0:
                    print("Logout berhasil")
                    break
                else:
                    print("Pilihan tidak tersedia!")
                    input("\ntekan enter untuk lanjut...")
                    os.system('cls || clear')


    elif pilih == 2 :   #done
        print("REGISTER")
        print("-" *80)
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
            key_baru = role
            akun.update({key_baru: {"username": username, "password": password}})
            # akun.append([username, password, role])
            print(f"Akun {username} berhasil di buat")
        input("\ntekan enter untuk lanjut...")
        os.system('cls || clear')
    else:
        break
    print("anda berhasil keluar")