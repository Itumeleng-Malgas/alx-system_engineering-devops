#!/usr/bin/python3
"""Script that uses the requests module"""
import json
import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetches employee data from the JSONPlaceholder API.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee_data = response.json()
    return employee_data


def fetch_todo_list(employee_id):
    """
    Fetches the list of todos for a specific employee from the
    JSONPlaceholder API.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todo_list = response.json()
    return todo_list


def display_todo_progress(employee_id):
    """
    Displays the progress of todos for a specific employee.
    """
    employee_data = fetch_employee_data(employee_id)
    todo_list = fetch_todo_list(employee_id)

    employee_username = employee_data.get('username')

    export_to_json(employee_id, employee_username, todo_list)


def export_to_json(employee_id, employee_username, todo_list):
    """
    Exports the employee's todo list to a JSON file.
    """
    json_filename = f"{employee_id}.json"
    tasks = [{"task": task["title"], "completed": task["completed"],
             "username": employee_username} for task in todo_list]
    data = {employee_id: tasks}

    with open(json_filename, mode='w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    display_todo_progress(employee_id)
