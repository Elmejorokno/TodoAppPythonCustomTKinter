import customtkinter as tk

def register_window(root):
    checked_password = False

    def handle_register():
        pass

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
    app.title("DoIt - Registrarse")
    app.geometry("400x400")

    app.protocol("WM_DELETE_WINDOW", handle_close)

    label_username = tk.CTkLabel(app, text="Username:", font=("Arial", 20, "bold"), text_color="#fff")
    label_username.place(relx=0.08, rely=0.1)
    entry_username = tk.CTkEntry(app, text_color="#fff")
    entry_username.place(relx=0.44, rely=0.1)

    label_password = tk.CTkLabel(app, text="Contraseña:", font=("Arial", 20, "bold"), text_color="#fff")
    label_password.place(relx=0.08, rely=0.2)
    entry_password = tk.CTkEntry(app, text_color="#fff", show="*")
    entry_password.place(relx=0.44, rely=0.2)

    checkbox_password = tk.CTkCheckBox(app, text="Mostrar contraseña", fg_color="#942492",
                                       checkbox_width=20, checkbox_height=20, command=handle_showpassword)
    checkbox_password.place(relx=0.62, rely=0.32, anchor='center')

    button_login = tk.CTkButton(app, text='Registrarse', corner_radius=20, fg_color="transparent",
                                hover_color="#942492",
                                border_color="#942492", border_width=2, command=handle_register)
    button_login.place(relx=0.5, rely=0.45, anchor='center')

    button_comeback = tk.CTkButton(app, text='Regresar', corner_radius=20, fg_color="transparent",
                                hover_color="#942492",
                                border_color="#942492", border_width=2, command=handle_comeback)
    button_comeback.place(relx=0.5, rely=0.55, anchor='center')

