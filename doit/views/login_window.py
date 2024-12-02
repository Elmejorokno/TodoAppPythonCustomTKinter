import customtkinter as tk

from doit.controllers.user_controller import login_user
from doit.views.tasks_window import tasks_window


def login_window(root):

    def handle_login():
        user, msg = login_user(entry_username.get(), entry_password.get())

        label_error_password.configure(text="")
        label_error_username.configure(text="")

        if user:
            app.withdraw()
            tasks_window(user, root)
        else:
            if msg == "Contraseña incorrecta.":
                label_error_password.configure(text=msg)
            elif msg == "Usuario no encontrado.":
                label_error_username.configure(text=msg)

    def handle_comeback():
        app.destroy()
        root.deiconify()

    def handle_showpassword():
        if checkbox_password.get():
            entry_password.configure(show="")
        else:
            entry_password.configure(show="*")

    def handle_close():
        app.destroy()
        root.destroy()

    app = tk.CTkToplevel(root)
    app.title("DoIt - Iniciar Sesión")
    app.geometry("430x400")

    app.protocol("WM_DELETE_WINDOW", handle_close)

    label_welcome = tk.CTkLabel(app, text="¡Bienvenido de vuelta 💼!", text_color="#fff", anchor="w", justify="left",
             font=("Arial", 30, "bold"))
    label_welcome.place(relx=0.08, rely=0.04)

    label_username = tk.CTkLabel(app, text="Username:", font=("Arial", 18, "bold"), text_color="#fff")
    label_username.place(relx=0.08, rely=0.18)
    entry_username = tk.CTkEntry(app, text_color="#fff", width=175)
    entry_username.place(relx=0.08, rely=0.26)

    label_error_username = tk.CTkLabel(app, text="", font=("Arial", 14, "bold"), text_color="red")
    label_error_username.place(relx=0.08, rely=0.335)

    label_password = tk.CTkLabel(app, text="Contraseña:", font=("Arial", 18, "bold"), text_color="#fff")
    label_password.place(relx=0.08, rely=0.42)
    entry_password = tk.CTkEntry(app, text_color="#fff", show="*", width=175)
    entry_password.place(relx=0.08, rely=0.5)

    checkbox_password = tk.CTkCheckBox(app, text="Mostrar contraseña", fg_color="#942492",
                                       checkbox_width=20, checkbox_height=20, command=handle_showpassword)
    checkbox_password.place(relx=0.54, rely=0.505)

    label_error_password = tk.CTkLabel(app, text="", font=("Arial", 14, "bold"), text_color="red")
    label_error_password.place(relx=0.08, rely=0.575)

    button_login = tk.CTkButton(app, text='Iniciar Sesión', corner_radius=20, fg_color="transparent",
                                hover_color="#942492", border_color="#942492", border_width=2, command=handle_login)
    button_login.place(relx=0.5, rely=0.7, anchor='center')

    button_comeback = tk.CTkButton(app, text='Regresar', corner_radius=20, fg_color="transparent",
                                hover_color="#942492", border_color="#942492", border_width=2, command=handle_comeback)
    button_comeback.place(relx=0.5, rely=0.8, anchor='center')

