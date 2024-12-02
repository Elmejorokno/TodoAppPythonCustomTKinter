import customtkinter as tk

from doit.views.login_window import login_window
from doit.views.register_window import register_window

def home_window():
    def handle_register():
        app.withdraw()
        register_window(app)

    def handle_login():
        app.withdraw()
        login_window(app)

    def handle_exit():
        app.destroy()

    app = tk.CTk()
    app.geometry('300x300')
    app.title("DoIt - Inicio")

    label_application = tk.CTkLabel(app, text="DoIt", font=("Arial", 50, "bold"), text_color="#942492")
    label_application.place(relx=0.5, rely=0.15, anchor="center")

    button_register = tk.CTkButton(app, text='Registrarse', corner_radius=20, fg_color="transparent", hover_color="#942492",
                                border_color="#942492", border_width=2, command=handle_register)
    button_register.place(relx=0.5, rely=0.35, anchor='center')

    button_login = tk.CTkButton(app, text='Iniciar Sesión', corner_radius=20, fg_color="transparent", hover_color="#942492",
                                border_color="#942492", border_width=2, command=handle_login)
    button_login.place(relx=0.5, rely=0.47, anchor='center')


    # Ejecutar la aplicación
    app.mainloop()
