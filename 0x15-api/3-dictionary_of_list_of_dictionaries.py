#!/usr/bin/python3
""" Retrieves all user data """
import json
import requests

# Fetching tasks data from the API
tasks_response = requests.get("https://jsonplaceholder.typicode.com/todos")
tasks = tasks_response.json()

# Fetching user data from the API
users_response = requests.get("https://jsonplaceholder.typicode.com/users")
users = users_response.json()

usernames_dict = {user['id']: user['username'] for user in users}

tasks_by_user = {}
for task in tasks:
    user_id = task['userId']
    username = usernames_dict.get(user_id, f"USER_{user_id}")

    if user_id not in tasks_by_user:
        tasks_by_user[user_id] = []

    tasks_by_user[user_id].append({
        "username": username,
        "task": task['title'],
        "completed": task['completed']
    })

# Creating the final dictionary with user ID as keys
result = ({str(user_id): tasks_list for user_id,
          tasks_list in tasks_by_user.items()})

# Writing the dictionary to a JSON file
with open("todo_all_employees.json", "w") as json_file:
    json.dump(result, json_file, indent=4)
