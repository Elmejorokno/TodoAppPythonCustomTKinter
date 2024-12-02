def check_credentials(username, password):
    if len(username) < 3 or len(username) > 10:
        return False, "Ingresa un nombre de usuario entre 3 y 10 carácteres."

    if len(password) < 8 or len(password) > 20:
        return False, "Ingresa una contraseña entre 8 y 20 carácteres."

    return True, "Todo bien"