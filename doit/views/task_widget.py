import customtkinter as tk

from doit.controllers.task_controller import toggle_task, delete_task
from doit.controllers.user_controller import update_user

#crea el widget para cada tarea
def create_task_widget(user, task, scrollable_frame, view_type="tasks"):
    remove_empty_message(scrollable_frame)

    def handle_toggle_task():
        toggle_task(task)
        update_user(user)

        if view_type == "tasks":
            if task["completed"]:
                task_frame.pack_forget()
        else:
            if task["completed"]:
                checkbox_task.select()
            else:
                checkbox_task.deselect()

    def handle_delete_task():
        delete_task(user, task)
        update_user(user)

        task_frame.pack_forget()

        # Revisa si hay tareas, si no hay, muestra el mensaje de vacio
        check_empty_tasks(user, scrollable_frame)

    task_frame = tk.CTkFrame(master=scrollable_frame, corner_radius=8, fg_color="#942492")
    task_frame.pack(fill="x", anchor="w", pady=(0, 20), padx=(5, 20))


    completed = tk.BooleanVar(value=task["completed"])
    checkbox_task = tk.CTkCheckBox(master=task_frame, fg_color="#942492", checkmark_color="#2A55B8", border_color="#fff",
                    hover_color="#A6C1FF", text=task["task_name"], variable=completed, command=handle_toggle_task)
    checkbox_task.pack(side="left", padx=(16, 20), pady=(8, 8))

    button_delete_task = tk.CTkButton(task_frame, text="✖️", corner_radius=20, fg_color="transparent",
                               hover_color="#942492", font=("Arial", 30),
                               cursor="hand2", command=handle_delete_task)
    button_delete_task.pack(pady=5, padx=10, side="right")

    return task_frame

#crea todas las tareas de un usuario en un scrollableFrame
def create_tasks_from_user(user, scrollable_frame, show_completed = False, view_type="tasks"):
    for task in scrollable_frame.winfo_children():
        task.destroy()

    check_empty_tasks(user, scrollable_frame)

    for task in user["tasks"]:
        if show_completed or not task["completed"]:
            create_task_widget(user, task, scrollable_frame, view_type)

    return scrollable_frame

def get_scrollable_frame(parent, frame=None):
    if frame is None or not frame.winfo_exists():
        frame = tk.CTkScrollableFrame(parent, width=1000, height=300, corner_radius=10)
        frame.pack(pady=(10, 0), fill="both", expand=True)
    return frame

#verifica si el usuario tiene tareas o no. muestra mensaje si no
def check_empty_tasks(user, scrollable_frame):
    if not user["tasks"]:  # Si no hay tareas
        # Mostrar emoji y mensaje
        label_emoji = tk.CTkLabel(scrollable_frame,text="🎉", font=("Arial", 150, "bold"), text_color="#942492")
        label_emoji.pack(pady=(50, 10))

        label_message = tk.CTkLabel(scrollable_frame, text="¡Parece que no tienes tareas!", font=("Arial", 20),
                                    text_color="#666")
        label_message.pack()

#elimina el mensaje de vacio (si es que hay)
def remove_empty_message(scrollable_frame):
    for widget in scrollable_frame.winfo_children():
        if isinstance(widget, tk.CTkLabel) and widget.cget("text") == "¡Parece que no tienes tareas!":
            widget.pack_forget()
        if isinstance(widget, tk.CTkLabel) and widget.cget("text") == "🎉":
            widget.pack_forget()

