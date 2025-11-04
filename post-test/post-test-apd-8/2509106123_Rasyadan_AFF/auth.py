from data import akun, username_exists
from next import nxt

def register():
    print("REGISTER")
    print("-" * 80)
    username = input("Buat user name: ")

    if username_exists(username):
        print("Nama sudah dipakai!")
    else:
        password = input("Buat password: ")
        akun["user"].append({"username": username, "password": password, "role": "user"})
        print(f"Akun {username} berhasil dibuat")
    nxt()

def add_account():
    print("Tambah akun")
    print("-" * 80)
    username = input("Buat user name: ")

    if username_exists(username):
        print("Nama sudah dipakai!")
    else:
        password = input("Buat password: ")
        print("[0] Admin\n[1] User")
        pilih = input(": ")
        while not pilih.isdigit() or int(pilih) not in [0, 1]:
            pilih = input("Pilih 0/1: ")

        role = "admin" if int(pilih) == 0 else "user"
        akun[role].append({"username": username, "password": password, "role": role})
        print(f"Akun {username} berhasil dibuat")
    nxt()

def login():
    print("LOGIN")
    print("-" * 80)
    username = input("Username: ")
    password = input("Password: ")

    for role, lst in akun.items():
        for db in lst:
            if db["username"] == username and db["password"] == password:
                print(f"Login berhasil sebagai {role.capitalize()}")
                nxt()
                return role

    print("Username / password salah")
    nxt()
    return None