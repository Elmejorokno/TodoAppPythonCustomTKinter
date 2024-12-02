import base64
import bcrypt

def encrypt_password(password):
    #Generar el hash de la contraseña
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

    #convertir el hash a base64 para que se pueda guardar en el JSON
    hashed_password_base64 = base64.b64encode(hashed_password).decode("utf-8")
    return hashed_password_base64

def check_password(password, hashed_password_base64):
    #convertir el base64 a bytes
    hashed_password = base64.b64decode(hashed_password_base64)

    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)

