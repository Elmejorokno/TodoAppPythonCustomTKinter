from doit.utils import data_manager
from doit.utils.password_utils import encrypt_password, check_password
from doit.validators.userValidator import check_credentials
import os


def register_user(username, password):
    file_path = os.path.join(os.path.dirname(__file__), "../users.json")
    users = data_manager.load_users(file_path)

    condition, message = check_credentials(username, password)

    if not condition:
        return None, message

    for user in users:
        if username == user["username"]:
            return None, "El usuario ya existe."

    encrypted_password = encrypt_password(password)

    new_user = {
        "username": username,
        "password": encrypted_password,
        "tasks": []
    }

    users.append(new_user)

    data_manager.save_data(file_path, users)

    return new_user, "Usuario registrado correctamente."


def login_user(username, password):
    file_path = os.path.join(os.path.dirname(__file__), "../users.json")
    users = data_manager.load_users(file_path)

    for user in users:
        if username == user["username"]:
            if check_password(password, user["password"]):
                return user, "Inicio de sesión exitoso."
            return None, "Contraseña incorrecta."
    return None, "Usuario no encontrado."


def update_user(user):
    file_path = os.path.join(os.path.dirname(__file__), "../users.json")
    users = data_manager.load_users(file_path)

    for i, act_user in enumerate(users):
        if user["username"] == act_user["username"]:
            users[i] = user
            data_manager.save_data(file_path, users)

    return user
