def login(username, password):
    if username == "admin" and password == "admin123":
        return "admin"
    elif username.startswith("69"):
        return "student"
    return None