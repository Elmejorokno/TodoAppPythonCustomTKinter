import customtkinter as tk

from doit.controllers.task_controller import add_task_to_user
from doit.controllers.user_controller import update_user
from doit.views.task_widget import create_task_widget, create_tasks_from_user, get_scrollable_frame
from doit.views.tasks_history_window import tasks_history_window


def tasks_window(user, root):
    def handle_add_task():
        task = add_task_to_user(user, entry_task.get())
        update_user(user)

        create_task_widget(user, task, scrollable_frame)

        entry_task.delete(0, "end")

    #muestra u oculta el menu despegable
    def handle_toggle_menu():
        if menu_frame.winfo_ismapped():
            menu_frame.place_forget()
        else:
            menu_frame.place(relx=0.845, rely=0.075)
            menu_frame.lift() #se muestra por encima de todos los elementos

    def handle_show_history():
        handle_toggle_menu()
        tasks_history_window(user, app, scrollable_frame)
        app.withdraw()

    def handle_logout():
        root.deiconify()
        app.destroy()

    def handle_close():
        app.destroy()
        root.destroy()

    app = tk.CTkToplevel(root)
    app.title("DoIt - Tareas")
    app.geometry("1000x600")
    app.protocol("WM_DELETE_WINDOW", handle_close)

    # -----Header------
    header_frame = tk.CTkFrame(app)
    header_frame.pack(fill="x", pady=(0, 10))

    label_application = tk.CTkLabel(header_frame, text="DoIt", font=("Arial", 40, "bold"), text_color="#942492")
    label_application.pack(side="left", padx=10)

    # boton para desplegar el menu
    button_user = tk.CTkButton(header_frame, text=user["username"], corner_radius=20, fg_color="transparent",
                                hover_color="#942492", border_color="#942492", border_width=2, command=handle_toggle_menu)
    button_user.pack(pady=10, padx=10, side="right")

    # Crear marco para el menú desplegable
    menu_frame = tk.CTkFrame(app, corner_radius=10)

    # Botones del menú
    button_task_history = tk.CTkButton(menu_frame, text="Mostrar historial", corner_radius=20, fg_color="transparent",
                                hover_color="#942492", border_color="#942492", border_width=2, command=handle_show_history)
    button_task_history.pack(padx=5)

    button_logout = tk.CTkButton(menu_frame, text="Cerrar sesión", corner_radius=20, fg_color="transparent",
                                hover_color="#942492", border_color="#942492", border_width=2, command=handle_logout)
    button_logout.pack(pady=(3, 0), padx=5)

    # ---------------Sección para añadir nuevas tareas---------------------
    add_task_frame = tk.CTkFrame(app, height=50)
    add_task_frame.pack(fill="x", pady=10)

    entry_task = tk.CTkEntry(add_task_frame, placeholder_text="Nueva tarea", width=600)
    entry_task.pack(side="left", padx=20, pady=10)

    add_task_button = tk.CTkButton(add_task_frame, text='Añadir tarea', corner_radius=20, fg_color="transparent",
                                   hover_color="#942492", border_color="#942492", border_width=2,
                                   command=handle_add_task)
    add_task_button.pack(side="left", padx=10)

    scrollable_frame = get_scrollable_frame(app)
    create_tasks_from_user(user, scrollable_frame)
