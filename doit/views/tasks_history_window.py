import customtkinter as tk

from doit.views.task_widget import create_tasks_from_user, get_scrollable_frame


def tasks_history_window(user, root, scrollable_frame_parent):
    def handle_close():
        app.destroy()
        create_tasks_from_user(user, scrollable_frame_parent)
        root.deiconify()

    app = tk.CTkToplevel(root)
    app.title("DoIt - Historial de tareas")
    app.geometry("1000x600")
    app.protocol("WM_DELETE_WINDOW", handle_close)

    scrollable_frame = get_scrollable_frame(app)
    create_tasks_from_user(user, scrollable_frame, True, "history")