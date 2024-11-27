import todo_controller
from todo import data_manager

users = data_manager.load_users("users.json")

def register_user(username, password):
    for user in users:
        if username == user["username"]:
            print("el usuario ya existe.")
            return None, "El usuario ya existe."

    new_user = {
        "username": username,
        "password": password,
        "todo": []
    }

    users.append(new_user)

    data_manager.save_data("users.json", users)

    return new_user, "Usuario registrado correctamente."


def login_user(username, password):
    for user in users:
        if username == user["username"]:
            if password == user["password"]:
                print("exitoso")
                return user, "Inicio de sesión exitoso."
            return None, "Contraseña incorrecta."
    return None, "Usuario no encontrado."

def update_user(user):
    for i, act_user in enumerate(users):
        if user["username"] == act_user["username"]:
            users[i] = user
            data_manager.save_data("users.json", users)

    return user


user, msg = login_user("ferdy", "24062005")
todo_controller.add_todo(user, "hacer video ingles")
update_user(user)

