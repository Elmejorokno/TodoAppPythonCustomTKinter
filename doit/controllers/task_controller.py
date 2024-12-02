def add_task_to_user(user, task_name, completed = False):
    task = {
        "task_name": task_name.strip(),
        "completed": completed
    }

    user["tasks"].append(task)
    return task

def toggle_task(task):
    task["completed"] = not task["completed"]

    return task

def delete_task(user, task):
    user["tasks"].remove(task)
