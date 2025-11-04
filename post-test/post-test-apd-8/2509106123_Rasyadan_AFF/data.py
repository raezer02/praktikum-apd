# data base

akun = {
    "admin": [{"username": "etmin", "password": "god", "role": "admin"}],
    "user": [{"username": "rakyat", "password": "nigen", "role": "user"}]
}

game = {
    "Roblox": {"genre": "game", "tahun": "2007"},
    "Mobilegend": {"genre": "Moba", "tahun": "2006"}
}

def username_exists(username):
    for role_list in akun.values():
        for a in role_list:
            if a["username"] == username:
                return True
    return False