import json

def load_users(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [] #return an empty list if there is no data

def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)