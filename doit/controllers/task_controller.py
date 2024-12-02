def add_task_to_user(user, name_todo, completed = False):
    todo = {
        "name_todo": name_todo,
        "completed": completed
    }

    user["todo"].append(todo)
    print(user)