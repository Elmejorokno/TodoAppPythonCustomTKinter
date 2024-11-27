import customtkinter as tk

from todo.views.login_window import login_window
from todo.views.register_window import register_window


def home_window():
    def handle_register():
        app.destroy()
        register_window()

    def handle_login():
        app.destroy()
        login_window()

    def handle_exit():
        app.destroy()

    app = tk.CTk()
    app.geometry('300x300')

    button_register = tk.CTkButton(app, text='Registrarse', corner_radius=20, command=handle_register)
    button_register.place(relx=0.5, rely=0.2, anchor='center')

    button_login = tk.CTkButton(app, text='Iniciar Sesión', corner_radius=20, command=handle_login)
    button_login.place(relx=0.5, rely=0.4, anchor='center')


    # Ejecutar la aplicación
    app.mainloop()
